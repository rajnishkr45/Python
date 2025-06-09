text_data = input("Enter the message want to store in a file: ")

f = open("myfile.txt","w") # if file name doesn't exist then it creates by itself 
f.write(text_data) 
f.close()

