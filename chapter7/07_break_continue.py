# Break statement

for i in range(100):
    if (i == 42):
        break  # Loop will exit if the value of i will 42 and no further execution takes place
    print(i)

# Continue statement
for i in range(100):
    if (i == 42):
        continue  # Loop will not exit but it will skip the code down the continue statement and it will go to next iteration Here 42 will not be printed
    print(i)


# Pass statement
for i in range(641): # here for loop will do nothing generally we write pass statement to skip the indentation error and further code is executed
    pass

i = 0
while (i < 5):
    print(i)
    i += 1
