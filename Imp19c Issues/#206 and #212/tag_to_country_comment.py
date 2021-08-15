from country_tag import *

country_array: list = [] 
commented: bool = False;

"""
Requires two iterations to fully parse the file,
First Iteration adds comments,
Second Iteration formats it properly
"""

with open("00_pre_scripted_countries.txt", "r",  encoding='utf-8') as countries:
    country_array =  countries.readlines();
with open("00_pre_scripted_countries.txt", "w",  encoding='utf-8') as countries:
    for line in country_array:
        if line != "\n":
            if len(line.split()[0]) == 3 or len(line.split()[0]) == 4: # handle commented tags
                if(len(line.split()[0]) == 4):
                    commented = True # commented tag
                tag = line.split()[0].strip("#")
                if(tag_dictionary[tag] in line):
                    if commented == True:
                        countries.write("#" + tag + " = {" + line.split("{")[1]) # add comment in front since it commented
                    else:
                        countries.write(tag + " = {" + line.split("{")[1]) # format it with spacing and keep all comments in front of opening
                    commented = False
                else:
                    countries.write(line.strip() + " #" + tag_dictionary[tag] + "\n") # append country behind the line
                continue
        countries.write(line)

        
            
