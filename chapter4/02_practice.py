i = 1
marks = []
while i <= 7:
    mark = int(input(f"Enter the marks {i}: "))
    marks.append(mark)
    i = i + 1

marks.sort()

print(marks)
