# create a class to store the data of programmers


class programmers:
    company = "Microsoft"
    name = None
    post = None
    language = None
    salary = None

    def __init__(self, name, post, language, salary):
        self.name = name
        self.post = post
        self.language = language
        self.salary = salary


rajnish = programmers("Rajnish", "CEO", "Python", 12489240)

print(rajnish.company, rajnish.name, rajnish.post, rajnish.language, rajnish.salary)
