# Module 11 Lab Exercise 9.2: Class average
# Conor Long
# 7/19/2024
# This program takes the "grades.txt" file and calculates the total of the grades stored, the number of grades stored, and the average of all grades.

# Initialize variables for calculation.
grades = []
total = 0
count = 0

# Opens the "grades.txt" file in read mode ('r').
with open('grades.txt', 'r') as f:
    
    # Read all lines from the file.
    lines = f.readlines()

# Process each line (each grade) read from the file.
for line in lines:
    
    # Strip any extra whitespace and convert to integer.
    grade = int(line.strip())
    grades.append(grade)
    total += grade
    count += 1

# Calculates the average of the grades.
average = total / count if count > 0 else 0

# Displays the grades in the file.
print("Individual Grades:")
for grade in grades:
    print(grade)

# Displays the grades' total.
print("\nTotal:", total)

# Displays the number of grades.
print("Count:", count)

# Displays the average of all of the grades.
print("Average:", average)
