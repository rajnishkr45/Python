# metods of making strings 

# single quote = 'Rajnish'
# Double quote = "Rajnish"
# Triple quote = '''Rajnish''' => multi line string

name = "Rajnish"

# Lenght of string 

stringLength = len(name)
print (stringLength)

# String Slicing => Getting a part of original string 

shortName = name[0:3] # It will return the starting 3 letters incuding 0th index and excluding 3rd index
print(shortName)

shortName1 = name[1:3] # it will include letter at 1 index and it will not include letter at 3 index
print (shortName1)

# Negative slicing 

# Negative slicing starts with -1 index and it is the last letter of string and it moves towards starting string in decreasing manner ie. -1, -2, -3 ...

