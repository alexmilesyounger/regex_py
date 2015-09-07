import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()


last_name = r'Love'
first_name = r'Kenneth'

# print(re.match(r'Love', data))
print(re.match(last_name, data)) # re.match() starts from the beginning of the string, so it will only match if the beginning of the string creates a match. 

# print(re.search(r'Kenneth', data))
print(re.search(first_name, data)) # re.search() works a bit like match, but it will review the entire string to find a match and does not requires the match to happen at the beginning of the string.