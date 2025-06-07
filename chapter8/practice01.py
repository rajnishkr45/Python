# function to find greatest number

def greatestOfAll(a,b,c):
    if(a > b and a > c):
        return f"{a} is the greates of all"
    elif(b > a and b > c):
        return f"{b} is greatest of all"
    elif(c > a and c > b):
        return f"{c} is greatest of all"
    else:
        return "all numbers are equal"

answer = greatestOfAll(2,6,9)
print(answer)