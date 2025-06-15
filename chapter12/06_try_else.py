try:
    num = int(input("Enter any number: "))
    print(num)

except Exception as e:
    print(e)

else:  # This will run when try block executes sucessfully
    print("Thank you")
