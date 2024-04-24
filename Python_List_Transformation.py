# Task 1: Given The List of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

#Sorting Grades
grades.sort()

#Calculating Grade Average
average = sum(grades)

# Replacing grades below 80 with 'Failed' value
if grades < 80:
    grades = "Failed"
    
