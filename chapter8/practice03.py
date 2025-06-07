def sumation(n):
    if(n == 1):
        return 1
    
    return n + sumation(n-1)

num = int (input("Enter the number to find the sum: "))
print(f"Sum of first {num} natural number is {sumation(num)}")