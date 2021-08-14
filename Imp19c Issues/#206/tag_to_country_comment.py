from country_tag import *

country_array = []
with open("00_pre_scripted_countries.txt", "r",  encoding='utf-8') as countries:
    country_array =  countries.readlines();
with open("00_pre_scripted_countries.txt", "w",  encoding='utf-8') as countries:
    for line in country_array:
        if line!="\n":
            if len(line.split()[0]) == 3: # if its tag
                countries.write(line.strip() + " #" + tag_dictionary[line.split()[0]] + "\n") # append country behind the line
                print(line.strip() + " #" + tag_dictionary[line.split()[0]] + "\n")
                continue
        countries.write(line)
        
            
