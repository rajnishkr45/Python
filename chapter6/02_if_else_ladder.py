age = int(input("Enter Your age: "))

# If elif else ladder

if age >= 18:
    print("You are above the age of consent !")
    print("Thats a great news !")

elif age < 0:
    print("You are entring negative which is not valid")
    print("Be aware of it")

else:
    print("You are below the age of consent !")
    print("Better luck next time")
