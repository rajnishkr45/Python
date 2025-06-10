class Employee:
    language = "Python"  # This is a class attibute
    salary = 10000000

    def getInfo(self):  # always pass self or any variable name
        print(f"The languange is {self.language} and the salary is {self.salary}")

    # Stactic methods that doesnot need any object or variable so to avoid error we use marker

    @staticmethod
    def greet():
        print("Good morning !")


rajnish = Employee()
rajnish.language = "JavaScript"
rajnish.getInfo()
rajnish.greet()


# when we call the methods of class it actually converts into Employee.getInfo(rajnish) and thats why it shows 1 argument passed
