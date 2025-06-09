# write a program to read a poem and check wether the word "twinkle" exist or not

with open("poem.txt", "r") as poem:
    data = poem.read()
    if "twinkle" in data.lower():
        print("The word twinkle is present in the poem")
    else:
        print("The word twinkle is NOT present in the poem")
