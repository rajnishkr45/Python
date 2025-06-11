class Employee:
    salary = 100000

    def increaseSalary(self, amount):
        self.salary = self.salary + amount

    def show(self):
        print(f"Your salary is {self.salary}")


a = Employee()

a.increaseSalary(50000)

a.show()
