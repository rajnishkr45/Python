a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

if b == 0:
    raise ZeroDivisionError("You cannot devide a number by zero")
else:
    print(a / b)
