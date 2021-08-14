country_array = []
region = [];
with open("countries.txt", "r", encoding='utf-8') as countries:
    country_array = countries.readlines();
with open("countries.txt", "w",  encoding='utf-8') as countries:
    for country in  country_array: 
        if (country != "\n" and country[0] != "#" and country.split()[0] != "REB" and                        # is not newline or comment
        country.split()[0] != "PIR" and country.split()[0] != "BAR"and country.split()[0] != "MER") : # REB, PIR, BAR and MER must be in the right order or it will crash
            region.append(country)
        else:
            region.sort() # sort in alphabetical order
            for tag in region:
                countries.write(tag);
            countries.write(country)
            region = []
    for tag in region: # if there are leftovers (for Polynesia)
            countries.write(tag);
    
    
        
    
    
