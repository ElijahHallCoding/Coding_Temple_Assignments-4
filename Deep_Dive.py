# Task 1: Given lists of students, their grades, and activities
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Task 1: Print students with grades below 80 along with their grade and activity
print("Students with grades below 80:")
for i in range(len(students)):
    if grades[i] < 80:
        print(students[i], grades[i], activities[i])

# Task 2: Create a list of approved students with grades above or equal to 80
students_approved = []
for i in range(len(students)):
    if grades[i] >= 80:
        students_approved.append(students[i])

# Task 3: Print the list of approved students
print("Approved students:", students_approved)