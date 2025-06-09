# replace all the censored words given in a list

words = ["donkey", "monkey", "dog", "cat"]

with open("donkey.txt", "r") as f:
    string = f.read()

for word in words:
    string = (string.lower()).replace(word, "#"*len(word))

with open("donkey.txt", "w") as f:
    f.write(string)

