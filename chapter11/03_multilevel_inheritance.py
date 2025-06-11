# Multilevel inheritance 

class Employee:
    a = 1

class Programmer(Employee):
    b = 2


class Manager(Programmer):
    c = 3
    

o = Manager()

print(o.a, o.b, o.c)