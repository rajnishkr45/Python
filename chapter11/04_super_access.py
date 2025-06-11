# super key word is used to access the constructor of parents class


class Employee:
    def __init__(self):
        print("I am constructor of Employee class")

    a = 1


class Programmer(Employee):
    def __init__(self):
        print("I am constructor of Programmer class")

    b = 2


class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("I am constructor of Manager class")

    c = 3


# o = Employee()
# p = Programmer()

# To access the parent constructor we will use super key word
q = Manager()

# print(o.a, o.b, o.c)
