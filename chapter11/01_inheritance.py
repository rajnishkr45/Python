# Inheritance


class Employee:
    company = "ITC"

    def getinfo(self):
        print(f"The employee name is {self.name} and the language is {self.language}")

    def getsalary(self):
        print(f"The salary of {self.name} is {self.salary}")


# may leads to error and can cause hectic

'''
class Programmers:
    company = "ITC Infotech"

# we need to access the same method that is defined in employee class
    def getinfo(self):
        print(f"The employee name is {self.name} and the language is {self.language}")
'''


# Instead of doning that all we simply use the methods of inheritance

class Programmer(Employee):  # Programmer class inherited all the methods and data of employee class
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The language of programmer is {self.languge}")


a = Employee()
b = Programmer()

print(a.company, b.company)
