country_array = []
region = [];
with open("countries.txt", "r", encoding='utf-8') as countries:
    country_array = countries.readlines();
with open("countries.txt", "w",  encoding='utf-8') as countries:
    for country in  country_array:
        if country != "\n" and country[0] != "#": # is not newline or comment
            region.append(country)
        else:
            region.sort() # sort in alphabetical order
            for tag in region:
                countries.write(tag);
            countries.write(country)
            region = []
    
    
        
    
    
