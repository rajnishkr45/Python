# To generate 1 to 20 table and store in different files in a folder



j = 1
while j <= 15:
    with open(f"table{j}.txt","a+") as table:
        for i in range(1,11):
            table.write(f"{j} X {i} = {j*i}\n")
    j += 1