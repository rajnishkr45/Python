# We will learn to read the external file

# open function takes two parameters 1st file name and 2nd mode ie. wether to read or write by default its read so even if we dont write mode it take r
f = open("file.txt", "r")  # open function is used to open the file
data = f.read()  # read function reads the content of file
print(data)
f.close()  # After accessing the content we must close the file


'''
methods of file

r -> read
w -> write
a -> append (To add something in pre existing files)

'''