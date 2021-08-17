import gspread
import pandas

SHEET_NAME = "character sheet sample"
TAG = "Country Tag"
ID = "CharacterID"

# Stored file in Windows for Bots https://docs.gspread.org/en/latest/oauth2.html
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
                    characters.write("}") #close the country tag
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
        """Define a new country tag to generate characters for"""
        
        characters.write('\"' + row[TAG] + '\"' + '={' + "\n")
        characters.write("\t" + "country=" + '\"' + row[TAG] + '\"' +  "\n")

    
    def name(self, row, characters):
        """Define id and full name of character"""
        
        characters.write("\t" + str(row[ID]) + "={" + "\n")
        characters.write("\t"*2 + "first_name=" +  '\"' + row["First Name"] + '\"' + "\n")
        if(row["Family"] != ""):
            characters.write("\t"*2 + "family = " +  '\"' + row["Family"] + '\"' + "\n")
        else:
            characters.write("\t"*2 + "family_name=" +  '\"' + row["Family Name"] + '\"' + "\n")
        if(row["Nickname"] != ""):
            characters.write("\t"*2 + "nickname=" +  '\"' + row["Nickname"]+ '\"' + "\n")

    
    def date(self, row, characters):
        """Define Birth and Death dates of character"""
        
        characters.write("\t"*2 + "birth_date=" + row["Birth Date"] + "\n")
        if(row["Death Date"]):
            characters.write("\t"*2 + "death_date=" + row["Death Date"] + "\n")

    
    def culture_religion(self, row, characters):
        """Define culture and religion, as well as point out if character is female"""
        
        characters.write("\t"*2 + "culture=" +  '\"' + row["Culture"].lower() + '\"' + "\n")
        characters.write("\t"*2 + "religion=" +  '\"' + row["Religion"].lower() + '\"' + "\n")
        if(row["Female"]):
            characters.write("\t"*2 + "female=yes" + "\n")
            
    def stats(self, row, characters):
        """Define Martial, Charisma, Finesse and Zeal stats for character"""
    
        if(row["Martial"] != ""):
            characters.write("\t"*2 + "add_martial=" + row["Martial"] + "\n")
        if(row["Charisma"] != ""):
            characters.write("\t"*2 + "add_charisma=" + row["Charisma"] + "\n")
        if(row["Finesse"] != ""):
            characters.write("\t"*2 + "add_finesse=" + row["Finesse"] + "\n")
        if(row["Zeal"] != ""):
            characters.write("\t"*2 + "add_zeal=" + row["Zeal"] + "\n")
        if(row["Martial"] != "" and row["Charisma"] != "" and row["Finesse"] != "" and row["Zeal"] != ""):
            characters.write("\t"*2 + "no_stats=yes" + "\n")

        
            

    def traits(self, row, characters):
        """Add traits if there are any, else let the game generate"""
        
        if(row["Traits"] != ""):
            characters.write("\t"*2 + "no_traits=yes" + "\n")
            trait_list = row["Traits"].split(",")
            for trait in trait_list:
                characters.write("\t"*2 + "add_trait=" + trait.strip() + "\n")
                
            


    def gold_popularity_prominence(self, row, characters):
        """Define gold, popularity and prominence"""
         
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
        """Define Paternal and Maternal relationship"""
        
        if(row["Father"] != ""):
            characters.write("\t"*2 + "father=char:" + row["Father"] + "\n")

        if(row["Mother"] != ""):
            characters.write("\t"*2 + "mother=char:" + row["Mother"] + "\n")

    def rulership(self, row, characters):
        """Define Rulers or Corulers"""
    
        if(row["Ruler"].strip() == "yes"):
            characters.write("\t"*2 + "c:" + row[TAG] + "={" + "\n")
            characters.write("\t"*3 + "set_as_ruler=char:" + str(row[ID]) + "\n")
            characters.write("\t"*2 + "}" + "\n")

        if(row["Coruler"].strip() == "yes"):
            characters.write("\t"*2 + "c:" + row[TAG] + "={" + "\n")
            characters.write("\t"*3 + "set_as_coruler=char:" + str(row[ID]) + "\n")
            characters.write("\t"*2 + "}" + "\n")

    def dna(self, row, characters):
        """Define DNA"""
        
        if(row["DNA"] != ""):
            characters.write("\t"*2 + "dna=" +  '\"' + row["DNA"] + '\"' + "\n")

    def closing(self, row, characters):
        """End character declaration"""
        
        characters.write("\t" + "}" + "\n")
        characters.write("\n")

Generator()

            
        
            
            
            
                
   

        
        
        
        
        
        
        
                         
        

