LAST_TAG = "HWI"

with open("countries.txt", "r", encoding='utf-8') as read_file:
    with open("country_tag.py", "w", encoding='utf-8') as write_file:
        write_file.write("tag_dictionary = {")
        for line in read_file:
            if(line == "\n" or line[0] == "#"):
                continue
            print(line.split())
            # accounting for \ufeff at the start of the file
            tag = line.split()[0][-3:]
            # accouting for comments on a line
            if (len(line.split()) > 3):
                country = line.split()[-2].split('.')[0].split('/')[-1]
            else:
                country = line.split()[-1].split('.')[0].split('/')[-1]
            if len(tag) == 3:
                write_file.write("\'"+tag+"\'"+": "+"\'"+ country + "\'")
            if(tag != LAST_TAG):
                write_file.write(", ")
        write_file.write("}")
                
              
        
