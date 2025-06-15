a = 89


def fun():
    # global a # It will make the local variable to global
    a = 3  # It is local variable for function and its value will be 3
    print(a)


fun()
print(a)
