languages = {}

i = 1
while i <= 4:
    name = input("Enter your name: ")
    lang = input("Enter your language: ")

    languages.update({name : lang})
    i = i + 1

print(languages)
