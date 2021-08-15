coat_of_arms_array: list = []
tag_start: int = 0
tag_end: int = 0
tag: str = ""
matrix_array: list = []
constant_matrix_array: list = []

with open("00_pre_scripted_countries.txt", "r", encoding='utf-8') as countries:
    coat_of_arms_array = countries.readlines();
length: int = len(coat_of_arms_array)
for number in range(length):
    line: str = coat_of_arms_array[number]
    if(line != "\n"): # if its not just a blank line
        if (len(line.split()[0]) == 3 or len(line.split()[0]) == 4): # to handle commented tags
            tag = line.split()[0][:3]
            tag_start = number # start of the tag line
        if(line == "}\n" or line == "} \n" or line == "#}\n" or line == "#} \n" or line == "}"): # to handle all closing brackets
            tag_end = number # end of the tagline
            if(tag == "REB" or tag == "PIR" or 
            tag == "BAR" or tag == "MER"):
                constant_matrix_array.append([tag, tag_start, tag_end])
            else:
                matrix_array.append([tag, tag_start, tag_end])
matrix_array.sort()

print(constant_matrix_array)
print(matrix_array)

with open("00_pre_scripted_countries.txt", "w", encoding='utf-8') as countries:
    for constant in constant_matrix_array:
        coat_of_arms = coat_of_arms_array[constant[1] : constant[2] + 1]
        for line in coat_of_arms:
            countries.write(line)
        countries.write("\n")
    for matrix in matrix_array:
        coat_of_arms = coat_of_arms_array[matrix[1] : matrix[2] + 1]
        for line in coat_of_arms:
            countries.write(line)
        countries.write("\n")
   
    

        
            
        
    
