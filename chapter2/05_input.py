# We will learn to take input form user

a = input("Enter 1st number: ")

b = input("Enter 2nd number: ")

print("Number 1 is: ", a)
print("Number 2 is: ", b)

print("Sum of both number is: ", a + b)

# Above code concatinate the value of a and b because by default input function takes string as input
# So we have to type cast the value of a and b into int so that we can perform any operation

# This will give us sum of a and b
print("Sum of a and b is: ", int(a) + int(b))
