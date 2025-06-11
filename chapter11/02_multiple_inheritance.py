# Multiple Inheritance => Inharit methods and data from more than one class


class Employee:
    company = "ITC"
    name = "Delafult name"
    language = "CPP"

    def getinfo(self):
        print(f"The employee name is {self.name} and the language is {self.language}")

    def getsalary(self):
        print(f"The salary of {self.name} is {self.salary}")


class Coder:
    language = "javascript"

    def showlanguages(self):
        print(f"out of many languagaes here is your language {self.language}")


class Programmer(
    Employee, Coder
):  # Programmer class inherited all the methods and data of employee class amd coder class
    company = "ITC Infotech"
    language = "Python"

    def showLanguage(self):
        print(f"The language of programmer is {self.language}")


a = Employee()
b = Programmer()

b.showLanguage()
b.showlanguages()
b.getinfo()
print(a.company, b.company)
