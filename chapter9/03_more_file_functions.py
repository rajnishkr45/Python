f = open("file.txt")

# data = f.readlines()  # readlines reads all lines and gives a list from it
# print(data, type(data))


# mean while read line reads single line and gives string
# data1 = f.readline()
# print(data1, type(data1))

# data2 = f.readline()
# print(data2, type(data2))

# data3 = f.readline()
# print(data3, type(data3))

# data4 = f.readline()  # nothing is present in line 4 so it will give an empty string
# print(data4 == "")

# Using while loop

line = f.readline()
while line != "":
    print(line)
    line = f.readline() # Here readline will work as iterator and it will keep moving to next line

f.close()
