name = "rajnish"

about = "Rajnish is a good good very good boy"

print(len(name))

print(name.capitalize())

print(name.lower())

print(name.upper())

print(
    about.replace("good", "bad")
)  # Replaces all the occurences here all "good" will be replaced by "bad"

print(
    name.startswith("Raj")
)  # It will return true is the string starts with given word else false

print(name.endswith("sh"))

# there are many more string functions avilable
"""
Function	             Description	                          Example
len()	            Returns the length of the string	    len("hello") → 5
str.lower()	        Converts to lowercase                	"HeLLo".lower() → 'hello'
str.upper()	        Converts to uppercase	                "hello".upper() → 'HELLO'
str.strip()	        Removes leading/trailing whitespace	    " hello ".strip() → 'hello'
str.lstrip()	    Removes leading whitespace	            " hello ".lstrip() → 'hello '
str.rstrip()	    Removes trailing whitespace	            " hello ".rstrip() → ' hello'
str.replace(a, b)	Replaces substring a with b	            "hello".replace("l", "x") → 'hexxo'
str.split()	        Splits string into list (by whitespace default)	"a b c".split() → ['a', 'b', 'c']
str.join(list)	    Joins list elements with string separator	" ".join(['a', 'b']) → 'a b'
str.find(sub)	    Returns index of first occurrence	    "hello".find("e") → 1
str.index(sub)	    Same as find(), but raises error if not found	"hello".index("e") → 1
str.startswith(sub)	Checks if string starts with sub	    "hello".startswith("he") → True
str.endswith(sub)	Checks if string ends with sub	        "hello".endswith("lo") → True
str.isalpha()	    Checks if all characters are letters	"abc".isalpha() → True
str.isdigit()	    Checks if all characters are digits	    "123".isdigit() → True
str.isalnum()	    Letters or digits only	                "abc123".isalnum() → True
str.isspace()	    Only whitespace	                        " \t\n".isspace() → True
str.capitalize()	First letter capitalized	            "hello".capitalize() → 'Hello'
str.title()	        Capitalize each word	                "hello world".title() → 'Hello World'
str.swapcase()	    Swap upper/lowercase	                "HeLLo".swapcase() → 'hEllO'
"""
