# Module 11 Lab Exercise 9.2: Class average
# Conor Long
# 7/19/2024
# This program takes the "grades.txt" file and calculates the total of the grades stored, the number of grades stored, and the average of all grades.

# Begins try block.
try:
    
    # Initialize variables for calculation.
    grades = []
    total = 0
    count = 0

    # Opens the "grades.txt" file in read mode ('r').
    with open('grades.txt', 'r') as f:
        
        # Reads all lines from the file.
        lines = f.readlines()

    # Processes each line (each grade) read from the file.
    for line in lines:

        # Begins try block.
        try:
            
            # Strip any extra whitespace and convert to integer.
            grade = int(line.strip())
            grades.append(grade)
            total += grade
            count += 1
            
        # Handles and prints a message for the ValueError exception.    
        except ValueError:
            print(f"Warning: Skipping invalid grade '{line.strip()}'")

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

# Handles and prints a message for the FileNotFoundError exception.
except FileNotFoundError:
    print("Error: File 'grades.txt' not found.")

# Handles and prints a message for the IOError exception.
except IOError as e:
    print(f"Error reading file: {e}")

# Handles and prints a message for the ZeroDivisionError exception.
except ZeroDivisionError:
    print("Error: Division by zero occurred.")

# Handles and prints a message or any other exception.
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Prints a completion message.
finally:
    print("Program execution completed.")
