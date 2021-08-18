import gspread
import pandas

SHEET_NAME = "character sheet sample"
TAG = "Country Tag"
ID = "CharacterID"

# Stored file in Windows for Bots https://docs.gspread.org/en/latest/oauth2.html
class Generator:
    
    def __init__(self):
        client = gspread.service_account(filename="service_account.json")
        sheet = client.open(SHEET_NAME).sheet1
        data = sheet.get_all_records()
        self.df= pandas.DataFrame(data)
        self.iterate()

    def iterate(self):
        tag = None # track whether the same country file is being edited
        self.characters = None
        for index, row in self.df.iterrows():
            self.row = row
            if (tag != self.row[TAG] or tag == None):
                tag = self.row[TAG]
                if (self.characters != None):
                    self.characters.write("}") #close the country tag
                    self.characters.close()
                self.characters = open("00_"+ self.row[TAG] + ".txt", "w", encoding="utf-8")
                self.new_country()
            self.name()
            self.date()
            self.culture_religion()
            self.stats()
            self.traits()
            self.gold_popularity_prominence()
            self.family()
            self.rulership()
            self.dna()
            self.closing()

    def new_country(self):
        """Define a new country tag to generate self.characters for"""
        
        self.characters.write('\"' + self.row[TAG] + '\"' + '={' + "\n")
        self.characters.write("\t" + "country=" + '\"' + self.row[TAG] + '\"' +  "\n")

    def name(self):
        """Define id and full name of character"""
        
        self.characters.write("\t" + str(self.row[ID]) + "={" + "\n")
        self.characters.write("\t"*2 + "first_name=" +  '\"' + self.row["First Name"] + '\"' + "\n")
        if(self.row["Family"] != ""):
            self.characters.write("\t"*2 + "family = " +  '\"' + self.row["Family"] + '\"' + "\n")
        else:
            self.characters.write("\t"*2 + "family_name=" +  '\"' + self.row["Family Name"] + '\"' + "\n")
        if(self.row["Nickname"] != ""):
            self.characters.write("\t"*2 + "nickname=" +  '\"' + self.row["Nickname"]+ '\"' + "\n")

    def date(self):
        """Define Birth and Death dates of character"""
        
        self.characters.write("\t"*2 + "birth_date=" + self.row["Birth Date"] + "\n")
        if(self.row["Death Date"]):
            self.characters.write("\t"*2 + "death_date=" + self.row["Death Date"] + "\n")

    def culture_religion(self):
        """Define culture and religion, as well as point out if character is female"""
        
        self.characters.write("\t"*2 + "culture=" +  '\"' + self.row["Culture"].lower() + '\"' + "\n")
        self.characters.write("\t"*2 + "religion=" +  '\"' + self.row["Religion"].lower() + '\"' + "\n")
        if(self.row["Female"]):
            self.characters.write("\t"*2 + "female=yes" + "\n")
            
    def stats(self):
        """Define Martial, Charisma, Finesse and Zeal stats for character"""
    
        if(self.row["Martial"] != ""):
            self.characters.write("\t"*2 + "add_martial=" + self.row["Martial"] + "\n")
        if(self.row["Charisma"] != ""):
            self.characters.write("\t"*2 + "add_charisma=" + self.row["Charisma"] + "\n")
        if(self.row["Finesse"] != ""):
            self.characters.write("\t"*2 + "add_finesse=" + self.row["Finesse"] + "\n")
        if(self.row["Zeal"] != ""):
            self.characters.write("\t"*2 + "add_zeal=" + self.row["Zeal"] + "\n")
        if(self.row["Martial"] != "" and self.row["Charisma"] != "" and self.row["Finesse"] != "" and self.row["Zeal"] != ""):
            self.characters.write("\t"*2 + "no_stats=yes" + "\n")

    def traits(self):
        """Add traits if there are any, else let the game generate"""
        
        if(self.row["Traits"] != ""):
            self.characters.write("\t"*2 + "no_traits=yes" + "\n")
            trait_list = self.row["Traits"].split(",")
            for trait in trait_list:
                self.characters.write("\t"*2 + "add_trait=" + trait.strip() + "\n")

    def gold_popularity_prominence(self):
        """Define gold, popularity and prominence"""
         
        if(self.row["Gold"] != ""):
            self.characters.write("\t"*2 + "add_gold=" + self.row["Gold"] + "\n")
        else:
            self.characters.write("\t"*2 + "add_gold=100" + "\n")
        if(self.row["Popularity"] != ""):
            self.characters.write("\t"*2 + "add_popularity=" + self.row["Popularity"] + "\n")
        else:
            self.characters.write("\t"*2 + "add_popularity=50" + "\n")

        if(self.row["Prominence"] != ""):
            self.characters.write("\t"*2 + "add_prominence=" + self.row["Prominence"] + "\n")

    def family(self):
        """Define Paternal and Maternal relationship"""
        
        if(self.row["Father"] != ""):
            self.characters.write("\t"*2 + "father=char:" + self.row["Father"] + "\n")

        if(self.row["Mother"] != ""):
            self.characters.write("\t"*2 + "mother=char:" + self.row["Mother"] + "\n")

    def rulership(self):
        """Define Rulers or Corulers"""
    
        if(self.row["Ruler"].strip() == "yes"):
            self.characters.write("\t"*2 + "c:" + self.row[TAG] + "={" + "\n")
            self.characters.write("\t"*3 + "set_as_ruler=char:" + str(self.row[ID]) + "\n")
            self.characters.write("\t"*2 + "}" + "\n")

        if(self.row["Coruler"].strip() == "yes"):
            self.characters.write("\t"*2 + "c:" + self.row[TAG] + "={" + "\n")
            self.characters.write("\t"*3 + "set_as_coruler=char:" + str(self.row[ID]) + "\n")
            self.characters.write("\t"*2 + "}" + "\n")

    def dna(self):
        """Define DNA"""
        
        if(self.row["DNA"] != ""):
            self.characters.write("\t"*2 + "dna=" +  '\"' + self.row["DNA"] + '\"' + "\n")

    def closing(self):
        """End character declaration"""
        
        self.characters.write("\t" + "}" + "\n")
        self.characters.write("\n")

Generator()
