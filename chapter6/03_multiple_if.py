age = int(input("Enter Your age: "))

# If statemsnts 1

if age % 2 == 0:
    print("age if even")

# End of if statement 1 and the above one is an independent statement

# start of if else statement 2
if age >= 18:
    print("You are above the age of consent !")
    print("Thats a great news !")

elif age < 0:
    print("You entered an invalid age !")
    print("Be aware of it !")

else:
    print("You are below the age of consent !")
    print("Better luck next time")

# End of if else statement 2 and it independent in it self no relation with if statement 1
