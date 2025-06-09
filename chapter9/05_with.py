#  we can get rid of every time closing the file after using it as it is possible that some time we can forget to use close function so we can use with

with open("file.txt") as f:
    print(f.read())

# no need to use close
