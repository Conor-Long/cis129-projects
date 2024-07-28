# MOdule 12 Lab: OOP Create a Pet Class
# Conor Long
# 7/28/2024
# This program prompts the user to input information about their pet, and then displays the information to the user.

# Defines the main function of the program. 
def main():

    # Creates a variable to store and reference the class, "pet".
    animal = pet()
    
    # Gets the pet's name from user input and updates the "pet.name" variable using a mutator with the information.
    inputName = input("Enter a pet name: ")
    animal.setName(inputName)
    
    # Gets the pet's type from user input and updates the "pet.type" variable using a mutator with the information.
    inputType = input("Enter a pet type: ")
    animal.setType(inputType)
    
    # Gets the pet's age from user input and updates the "pet.age" variable using a mutator with the information. 
    inputAge = int(input("Enter a pet age: "))
    animal.setAge(inputAge)

    # Displays the pet information values stored using accessors to retrieve the information. 
    print(f"The pet name is {animal.getName()}")
    print(f"The pet type is {animal.getType()}")
    print(f"The pet age is {animal.getAge()}")

# Defines a class which outlines different variables and statements for updating them.
class pet:
    
    # Initializes the petInfo variables for updating and retrieving their values later in the program. 
    def petInfo(pet, name="", type="", age=0):
        pet.name = name
        pet.type = type
        pet.age = age

    # Defines a set of mutators to update different petInfo values.
    def setName(pet, name):
        pet.name = name

    def setType(pet, type):
        pet.type = type

    def setAge(pet, age):
        pet.age = age

    # Defines a set of accessors to retrieve different petInfo values.
    def getName(pet):
        return pet.name

    def getType(pet):
        return pet.type

    def getAge(pet):
        return pet.age

# Starts the program.
main()