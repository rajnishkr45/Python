# Greatest of 4 numbers

num1 = int(input("Enter any number 1: "))
num2 = int(input("Enter any number 2: "))
num3 = int(input("Enter any number 3: "))
num4 = int(input("Enter any number 4: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"number 1 ie. {num1} is greates of all")

elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"number 2 ie. {num2} is greates of all")

elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"number 3 ie. {num3} is greates of all")

elif num4 > num1 and num4 > num2 and num4 > num3:
    print(f"number 4 ie. {num4} is greates of all")

else:
    print("All are equal")
