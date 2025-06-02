l1 = [1, 5, 7, 6, 2, 9, 11, 10, 15]

l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.append(14)  # It will add 14 at last
print(l1)

l1.insert(3, 45)  # 45 will be insterted at 4th position ie. 3rd index
print(l1)

l1.pop(5)  # 5th index item will be removed
print(l1)

l1.insert(3, 45)
l1.insert(3, 45)
l1.remove(
    45
)  # It removes the 1st given value from the list here it will remove 1st occurence of 45
print(l1)
