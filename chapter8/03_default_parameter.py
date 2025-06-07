# default parameter is the default value passed in parameter that get trigggred when the functionis called without any value

def sayHello(name = "Missing User"):
    print("Hello, "+ name)
    
sayHello("Rajnish") # here the function will print Hello rajnish as value is being passed
sayHello() # here no value is passed so the default value ie. Missing user will be used