# Module 11 Lab Exercise 9.1: Class Grades
# Conor Long
# 7/19/2024
# This program takes the user's input of seven grades and updates the text files "grades.txt" with the values.

# A list is created to store the grades.
grades = []

# Prints welcome message and prompt.
print("Welcome to the grade updater!\nPlease enter each of five grades:")

# Begins try block.
try:
    
    # Iterates the entry of seven class grades to the "grades" list.
    for i in range(1, 8):
        while True:
            try:
                
                # Converts the user's input to float.
                grade = float(input("Grade " + str(i) + ": "))

                # Checks if grade is in range.
                if 0 <= grade <= 100:
                    break
                else:
                    print("Grade must be between 0 and 100. Please try again.")

            # Handles the ValueError exception and prints a message.        
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Appends the "grades" list with the values entered.
        grades.append(grade)

    # Opens the "grades.txt" file in write mode.
    with open('grades.txt', 'w') as f:
        
        # Iterates over each grade in the "grades" list.
        for grade in grades:
            
            # Write each grade followed by a newline character.
            f.write(f'{grade}\n')

    # Prints a confirmation message
    print("Grades have been written to grades.txt")

# Handles and prints a message for the IOError exception.
except IOError as e:
    print(f"Error writing to file: {e}")

# Handles and prints a message for any other exception.
except Exception as e:
    print(f"An error occurred: {e}")

# Prints a completion message.
finally:
    print("Program execution completed.")
