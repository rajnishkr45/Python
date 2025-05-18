import os

# Variable
drictory_path = "D:\django\python"

# Content in a drictory 
contents = os.listdir(drictory_path)

# Printing all contents
for items in contents:
    print(items)