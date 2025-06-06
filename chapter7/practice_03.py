# number is prime or not

num = int(input("Enter any number: "))


for i in range(2,num):
    if(num % i == 0):
        print("Number is not a prime !")
        break
else:
    print("Number is prime !")
