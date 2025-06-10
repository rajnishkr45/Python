class Employee:
    language = "Python"  # This is a class attibute
    salary = 10000000

    #   init and all the functions starting with __ are aclled dunder method
    # Here __init__ function works as default constructor like in cpp
    def __init__(self, name, language, salary):
        print("I am creating an object")
        self.name = name
        self.language = language
        self.salary = salary


rajnish = Employee("Rajnish", "Javascript", 1500000)

print(rajnish.name, rajnish.language, rajnish.salary)


# instance attibute take over the class attibute when it is assigned any value
