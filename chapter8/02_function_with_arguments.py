# Here name and ending are the parameters that are being used as variable name in the function


def goodDay(name, ending):
    print(f"Welcome, {name}!\nHave a nice day")
    print(f"\t{ending}")


# Calling the function by passing two variables
goodDay("Rajnish", "Thank you")
goodDay("Ramu Kaka", "Thank you")
goodDay("Ramlal", "Thanks")

# Function can even return something that may be string or may be number or anything


def fun1(name):
    print(f"Hello, {name}")
    return "Bye"  # Here bye will be returned from function


a = fun1("Ramlal")
print(a)
