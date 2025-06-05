marks1 = int(input("Enter the marks of subject 1: "))
marks2 = int(input("Enter the marks of subject 2: "))
marks3 = int(input("Enter the marks of subject 3: "))

total_marks_obtained = marks1 + marks2 + marks3
total_marks = 300
percentage = (total_marks_obtained / total_marks) * 100

if (marks1 >= 33 and marks2 >= 33 and marks3 >= 33 and percentage >= 40):
    print("You passed the exam !")
    print("\tCongratulations !")

else:
    print("Your failed to pass the exam !")
    print("\tTry hard next time !")