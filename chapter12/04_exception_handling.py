# use to give customise error

# num = int(input("Enter any number: ")) # If we enter any character than number then it gives error so we will use exception handling

# print(num)

try:
    num = int(input("Enter any number: "))
    print(num)

except Exception as e:
    print(e)

print("Thank you")


# Multiple error segment

try:
    num = int(input("Enter any number: "))
    print(num)

except ValueError as v:
    print("This is value error !")
    print(v)

except Exception as e:
    print(e)

print("Thank you")
