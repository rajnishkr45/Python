# Factorial of n

n = int(input("Enter any number: "))

fact = 1
for i in range(1, n + 1):
    fact *= i
else:
    print(f"Factorial of the number {n} is {fact}")