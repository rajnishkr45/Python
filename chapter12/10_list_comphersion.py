lst = [1, 2, 5, 7, 8, 3, 6, 5]

# squaredList = []
# for item in lst:
#     squaredList.append(item * item)

# This can be done by list comphersion

squaredList = [i * i for i in lst]

print(squaredList)
