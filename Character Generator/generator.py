import gspread
import pandas

SHEET_NAME = "character sheet sample"
TAG = "Country Tag"
ID = "CharacterID"
# Stored file in Windows for Bots https://docs.gspread.org/en/latest/oauth2.html
# Use google.auth instead oauth2client since its deprecated
# https://youtu.be/cnPlKLEGR7E?t=346
"""
class SheetConnection():
    def __init__(self):
        credentials, project = google.auth.default(
        scopes =  ["https://spreadsheets.google.com/feeds",
                        "www.googleapis.com/auth/spreadsheets",
                        "https://www.googleapis.com/auth/drive.file",
                        "https://www.googleapis.com/auth/drive" ])
        client = gspread.authorize(credentials)
        sheet = client.open("character sheet sample").sheet1
        data = sheet.get_all_records()
        print(data)
"""    

class Generator:
    
    def __init__(self):
        client = gspread.service_account()
        sheet = client.open(SHEET_NAME).sheet1
        data = sheet.get_all_records()
        self.df= pandas.DataFrame(data)
        self.iterate()

    def iterate(self):
        tag = None
        characters = None
        for index, row in self.df.iterrows():
            if (tag != row[TAG] or tag == None):
                tag = row[TAG]
                if (characters != None):
                    characters.write("}")
                    characters.close()
                characters = open("00_"+ row[TAG] + ".txt", "w", encoding="utf-8")
                self.new_country(row, characters)
            self.name(row, characters)
            self.date(row, characters)
            self.culture_religion(row, characters)
            self.stats(row, characters)
            self.traits(row, characters)
            self.gold_popularity_prominence(row, characters)
            self.family(row, characters)
            self.rulership(row, characters)
            self.dna(row, characters)
            self.closing(row, characters)

    def new_country(self, row, characters):
        characters.write('\"' + row[TAG] + '\"' + '{=' + "\n")
        characters.write("\t" + "country=" + '\"' + row[TAG] + '\"' +  "\n")

    def name(self, row, characters):
        characters.write("\t" + str(row[ID]) + "={" + "\n")
        characters.write("\t"*2 + "first_name=" +  '\"' + row["First Name"] + '\"' + "\n")
        if(row["Family"] != ""):
            characters.write("\t"*2 + "family = " +  '\"' + row["Family"] + '\"' + "\n")
        else:
            characters.write("\t"*2 + "family_name=" +  '\"' + row["Family Name"] + '\"' + "\n")
            
    def date(self, row, characters):
        characters.write("\t"*2 + "birth_date=" + row["Birth Date"] + "\n")
        if(row["Death Date"]):
            characters.write("\t"*2 + "death_date=" + row["Death Date"] + "\n")
            
    def culture_religion(self, row, characters):
        characters.write("\t"*2 + "culture=" +  '\"' + row["Culture"] + '\"' + "\n")
        characters.write("\t"*2 + "religion=" +  '\"' + row["Religion"] + '\"' + "\n")
        if(row["Female"]):
            characters.write("\t"*2 + "female=yes" + "\n")
            
    def stats(self, row, characters):
        characters.write("\t"*2 + "no_stats=yes" + "\n")
        if(row["Martial"] != ""):
            characters.write("\t"*2 + "add_martial=" + row["Martial"] + "\n")
        if(row["Charisma"] != ""):
            characters.write("\t"*2 + "add_charisma=" + row["Charisma"] + "\n")
        if(row["Finesse"] != ""):
            characters.write("\t"*2 + "add_finesse=" + row["Finesse"] + "\n")
        if(row["Zeal"] != ""):
            characters.write("\t"*2 + "add_zeal=" + row["Zeal"] + "\n")

    def traits(self, row, characters):
        characters.write("\t"*2 + "no_traits=yes" + "\n")
        if(row["Traits"] != ""):
            trait_list = row["Traits"].split(",")
            for trait in trait_list:
                characters.write("\t"*2 + "add_trait=" + trait.strip() + "\n")

    def gold_popularity_prominence(self, row, characters):
        if(row["Gold"] != ""):
            characters.write("\t"*2 + "add_gold=" + row["Gold"] + "\n")
        else:
            characters.write("\t"*2 + "add_gold=100" + "\n")
            
        if(row["Popularity"] != ""):
            characters.write("\t"*2 + "add_popularity=" + row["Popularity"] + "\n")
        else:
            characters.write("\t"*2 + "add_popularity=50" + "\n")

        if(row["Prominence"] != ""):
            characters.write("\t"*2 + "add_prominence=" + row["Prominence"] + "\n")

    def family(self, row, characters):
        if(row["Father"] != ""):
            characters.write("\t"*2 + "father=char:" + row["Father"] + "\n")

        if(row["Mother"] != ""):
            characters.write("\t"*2 + "mother=char:" + row["Mother"] + "\n")

    def rulership(self, row, characters):
        if(row["Ruler"].strip() == "yes"):
            characters.write("\t"*2 + "c:" + row[TAG] + "={" + "\n")
            characters.write("\t"*3 + "set_as_ruler=char:" + str(row[ID]) + "\n")
            characters.write("\t"*2 + "}" + "\n")

        if(row["Coruler"].strip() == "yes"):
            characters.write("\t"*2 + "c:" + row[TAG] + "={" + "\n")
            characters.write("\t"*3 + "set_as_coruler=char:" + str(row[ID]) + "\n")
            characters.write("\t"*2 + "}" + "\n")

    def dna(self, row, characters):
        if(row["DNA"] != ""):
            characters.write("\t"*2 + "dna=" +  '\"' + row["DNA"] + '\"' + "\n")

    def closing(self, row, characters):
        characters.write("\t" + "}" + "\n")
        characters.write("\n")

Generator()
    
        

"""
for index, row in df.iterrows():
    with open("00_"+ row[TAG] + ".txt", "w", encoding="utf-8") as characters:
        characters.write('\"' + row[TAG] + '\"' + '{=' + "\n")
        characters.write("\t" + "country=" + '\"' + row[TAG] + '\"' +  "\n")

        characters.write("\t" + str(row[ID]) + "={" + "\n")
        characters.write("\t"*2 + "first_name=" +  '\"' + row["First Name"] + '\"' + "\n")
        if(row["Family"] != ""):
            characters.write("\t"*2 + "family = " +  '\"' + row["Family"] + '\"' + "\n")
        else:
            characters.write("\t"*2 + "family_name=" +  '\"' + row["Family Name"] + '\"' + "\n")
            
        characters.write("\t"*2 + "birth_date=" + row["Birth Date"] + "\n")
        if(row["Death Date"]):
            characters.write("\t"*2 + "death_date=" + row["Death Date"] + "\n")
            
        characters.write("\t"*2 + "culture=" +  '\"' + row["Culture"] + '\"' + "\n")
        characters.write("\t"*2 + "religion=" +  '\"' + row["Religion"] + '\"' + "\n")
        if(row["Female"]):
            characters.write("\t"*2 + "female=yes" + "\n")
        
        characters.write("\t"*2 + "no_stats=yes" + "\n")
        if(row["Martial"] != ""):
            characters.write("\t"*2 + "add_martial=" + row["Martial"] + "\n")
        if(row["Charisma"] != ""):
            characters.write("\t"*2 + "add_charisma=" + row["Charisma"] + "\n")
        if(row["Finesse"] != ""):
            characters.write("\t"*2 + "add_finesse=" + row["Finesse"] + "\n")
        if(row["Zeal"] != ""):
            characters.write("\t"*2 + "add_zeal=" + row["Zeal"] + "\n")
            
        characters.write("\t"*2 + "no_traits=yes" + "\n")
        if(row["Traits"] != ""):
            trait_list = row["Traits"].split(",")
            for trait in trait_list:
                characters.write("\t"*2 + "add_trait=" + trait.strip() + "\n")

        if(row["Gold"] != ""):
            characters.write("\t"*2 + "add_gold=" + row["Gold"] + "\n")
        else:
            characters.write("\t"*2 + "add_gold=100" + "\n")
            
        if(row["Popularity"] != ""):
            characters.write("\t"*2 + "add_popularity=" + row["Popularity"] + "\n")
        else:
            characters.write("\t"*2 + "add_popularity=50" + "\n")

        if(row["Prominence"] != ""):
            characters.write("\t"*2 + "add_prominence=" + row["Prominence"] + "\n")

        if(row["Father"] != ""):
            characters.write("\t"*2 + "father=char:" + row["Father"] + "\n")

        if(row["Mother"] != ""):
            characters.write("\t"*2 + "mother=char:" + row["Mother"] + "\n")

        if(row["Ruler"].strip() == "yes"):
            characters.write("\t"*2 + "c:" + row[TAG] + "={" + "\n")
            characters.write("\t"*3 + "set_as_ruler=char:" + str(row[ID]) + "\n")
            characters.write("\t"*2 + "}" + "\n")

        if(row["Coruler"].strip() == "yes"):
            characters.write("\t"*2 + "c:" + row[TAG] + "={" + "\n")
            characters.write("\t"*3 + "set_as_coruler=char:" + str(row[ID]) + "\n")
            characters.write("\t"*2 + "}" + "\n")

        if(row["DNA"] != ""):
            characters.write("\t"*2 + "dna=" +  '\"' + row["DNA"] + '\"' + "\n")

        characters.write("\t" + "}" + "\n")
        characters.write("\n")

        characters.write("}" + "\n")
"""
            
            
        
            
            
            
                
   

        
        
        
        
        
        
        
                         
        

