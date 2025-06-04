marks = {"Rajnish": 100, "Rajjjo": 85, "Ramu Kaka": 55, "Ramlal": 31}

print(marks.items())  # It will give a list that will store key value in form of tuples

print(marks.keys())  # It will print the list of keys

print(marks.values())  # It will print the list of values

marks.update(
    {"Rajnish": 99, "Chimtu": 55}
)  # It will update the existing values and add the missing values if not present

print(marks)  # Chimtu will be added

print(marks.get("Rajnish"))  # If key doesn't exixt it show none
print(marks["Rajnish"])  # If key doesn't exist it gives error

print(
    marks.pop("Ramu Kaka")
)  # Removes the given key and its value from any where in the dictionary
print(marks)

print(marks.popitem())  # Remove the last key value pair
print(marks)
