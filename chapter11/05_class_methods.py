class Students:
    no = 1

    #  To avoid the printing the object value we use 

    @classmethod
    def show(cls):
        print(f"The number of students in class attibute is: {cls.no}")


s = Students()

s.no = 45

s.show()
