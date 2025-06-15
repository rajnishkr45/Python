lst = [1, 3, 55, 563, 8767]


# index = 0
# for item in lst:
#     print(f"The item at index {index} is {item}")
#     index += 1

# This can be simplified by enumerate function

for index, item in enumerate(lst):
    print(f"The item at index {index} is {item}")
