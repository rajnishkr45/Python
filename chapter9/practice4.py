# replace all "donkey" words of a file with "####"

word = "donkey"

with open("donkey.txt", "r") as f:
    string = f.read()

new_string = (string.lower()).replace(word, "####")

with open("donkey.txt", "w") as f:
    f.write(new_string)
