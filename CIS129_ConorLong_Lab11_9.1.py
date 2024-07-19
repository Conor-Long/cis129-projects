# Module 11 Lab Exercise 9.1: Class Grades
# Conor Long
# 7/19/2024
# This program takes the user's input of seven grades and updates the text files "grades.txt" with the values.

# A list is created to store the grades.
grades = []

# Prints welcome message and prompt.
print("Welcome to the grade updater!\nPlease enter each of five grades:")

# Iterates the entry of seven class grades to the "grades" list.
for i in range(1, 8):
    grade = input("Grade " + str(i) + ": ")
    grades.append(grade)
        
# Opens the file in write mode.
with open('grades.txt', 'w') as f:
    
    # Iterate over each grade in the "grade" list.
    for grade in grades:
        
        # Write each grade followed by a newline character.
        f.write(f'{grade}\n')

# Prints text
print("Grades have been written to grades.txt")


