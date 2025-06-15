def myFun():
    print("This is my function")


print(__name__)

if __name__ == "__main__":
    print("I am directly run by the same file only")
    # it will not execute outside this code file
    myFun()
