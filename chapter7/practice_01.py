# table of given number

num = int(input("Enter any number: "))

for i in range(num, 11 * num, num):
    print(i)

# using while loop

i = 1
while i < 11:
    print(i * num)
    i += 1