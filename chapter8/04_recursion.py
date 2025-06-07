# calling the same function repeatidly

# Example factorial can be written as => fact(n) = n* fact(n-1)

def fact(n):
    if(n == 1 or n== 0):
        return 1
    
    return n*fact(n-1)

num = int(input("Enter any number: "))

print(fact(num))