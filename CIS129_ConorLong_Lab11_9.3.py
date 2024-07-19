# Module 11 Lab Exercise 9.3: Class csv
# Conor Long
# 7/19/2024
# This program takes multiple students' data as user inputs and stores that information in "grades.csv".

# Imports the csv module.
import csv

# Begins try block:
try:

    # Opens the file in write mode with newline='' to prevent extra newline characters.
    with open('grades.csv', 'w', newline='') as csvfile:
        
        # Creates and stores a CSV writer object in csv_writer.
        csvWriter = csv.writer(csvfile)
        
        # Writes the header row.
        csvWriter.writerow(['firstname', 'lastname', 'exam1grade', 'exam2grade', 'exam3grade'])
        
        # Gets number of students from the user's input.
        while True:
            try:
                
                # Number of student is input and stored in the studentsNum variable.
                studentsNum = int(input("Enter the number of students: "))

                # If studentsNum is zero or less, the program loops back.
                if studentsNum > 0:
                    break
                else:
                    print("Number of students must be greater than zero. Please try again.")

            # Handles the ValueError exception and prints a message.     
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # Iterates through each student to input their information.
        for i in range(1, studentsNum + 1):
            while True:
                try:
                    firstName = input(f"Enter first name of student {i}: ")
                    lastName = input(f"Enter last name of student {i}: ")
                    exam1Grade = int(input(f"Enter exam 1 grade of student {i}: "))
                    exam2Grade = int(input(f"Enter exam 2 grade of student {i}: "))
                    exam3Grade = int(input(f"Enter exam 3 grade of student {i}: "))
                    break

                # Handles the ValueError exception and prints a message.
                except ValueError:
                    print("Invalid input. Please enter a valid integer for exam grades.")

            # Write the student's information to the CSV file.
            csvWriter.writerow([firstName, lastName, exam1Grade, exam2Grade, exam3Grade])

    # Prints a confirmation message.
    print(f"Grades have been written to grades.csv")

# Handles and prints a message for the IOError exception.
except IOError as e:
    print(f"Error writing to file: {e}")

# Handles and prints a message for any other exception.
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Prints a completion message.
finally:
    print("Program execution completed.")
