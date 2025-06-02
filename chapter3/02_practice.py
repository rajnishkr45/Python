letter = '''Dear, <|Name|>
You are selected as developer please join us 
on <|Date|>'''

# Fill the name and date in above 

str1 = letter.replace("<|Name|>", "Rajnish")
str2 = str1.replace("<|Date|>", "05/06/2025")

print(str2)

