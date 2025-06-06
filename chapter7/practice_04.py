# Sum of n natural numbers using while loop

num = int(input("Enter any number: "))

i, sm = 1, 0
while i <= num:
    sm += i
    i += 1

print(f"Sum of first {num} natural number is {sm}")
