# Task 1 
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Find students who both submitted and attended
both_submitted_and_attended = set(submitted) & set(attended)

print("Students who both submitted and attended:", both_submitted_and_attended)

# Task 2
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Check if the lists are identical
identical = set(submitted) == set(attended)

print("Are the lists identical in terms of content?", identical)

# Task 3 
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Remove students from attended list who did not submit
attended = [student for student in attended if student in submitted]

print("Updated attended list:", attended)


