# #206

### Commenting of country names beside their tags

read_countries.py reads in all countries in countries.txt and writes a dictionary to country_tag.py.

Country's tag will be the key of the dictionary, while it's value will be the name of the country.

tag_to_country_comment.py will use the dictionary and add comments containing the country name beside the tags.

#### Requires two iterations to fully parse the file
1. First Iteration adds comments,
2. Second Iteration formats it properly

# #212 

### Sorting coat of arms in an alphabetical order

Two matrixes are used to carry out the operation.

One stores the constants, "REB", "BAR", "MER", "PIR"

The other stores the rest of the coat_of_arms.

It is stored in this format:
```
[ country_name: str , tag_start: int, tag_end: int]
```

The previous coat_of_arms file will be read and pointers will be assigned based on the start and end of a tag. 
It will be stored in a list.

The previous file information will also be stored in a list, which is how tag/country information is retrieved.

Afterwards, data from the list will be sorted in an alphabetical order and parsed for the coat_of_arms file to be overwritten. 
