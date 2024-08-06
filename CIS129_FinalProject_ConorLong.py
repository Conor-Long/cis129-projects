'''
Script: CIS129_FinalProject_ConorLong.py
Action: This program calculates the cost of planting a field of one of three optional crops. Using a grid (farm field), the program counts and caluclates the cost of the amount of seeds, weater, and fertilizer needed to fill every square (plot) in the grid (field).
Author: Conor Long
Date: 8/6/2024
'''

# Creates global dictionaries which contain the costs for each crop type.
seedCostDict = {'wheat': 10, 'corn': 6, 'sugarcane': 3}
cropDensityDict = {'wheat': 2, 'corn': 1, 'sugarcane': 3}
waterReqDict = {'wheat': 1, 'corn': 2, 'sugarcane': 3}
fertilizerReqDict = {'wheat': 1, 'corn': 2, 'sugarcane': 3}

# Defines a function which creates an empty grid (field).
def createField(rows, columns):
    field = []

    # Creates a grid of the specified size with default values.
    for r in range(rows):
        row = []
        for c in range(columns):
            cell = {'seeds': False, 'water': False, 'fertilizer': False}
            row.append(cell)
        field.append(row)
    
    # Returns the empty grid (field).
    return field

# Defines a function which simulates applying seeds, water, and fertilizer to the grid (field).
def applyResources(field, seedCost, waterCost, fertilizerCost, density, waterReq, fertReq):

    # Sets initial values for total costs.
    totalSeedCost = 0
    totalWaterCost = 0
    totalFertilizerCost = 0
    
    # Iterates over all grid spaces.
    for row in field:
        for cell in row:

            # Simulates applying seeds, water, and fertilizer.
            cell['seeds'] = True
            cell['water'] = True
            cell['fertilizer'] = True
            
            # Adds the cost of resources to the total cost.
            if cell['seeds']:
                totalSeedCost += seedCost * density
            if cell['water']:
                totalWaterCost += waterCost * waterReq
            if cell['fertilizer']:
                totalFertilizerCost += fertilizerCost * fertReq
    
    # Returns costs.
    return totalSeedCost, totalWaterCost, totalFertilizerCost

# Function to display the costs of resources used
def displayCosts(totalSeedCost, totalWaterCost, totalFertilizerCost):
    totalCost = totalSeedCost + totalWaterCost + totalFertilizerCost
    print(f"Total seed cost: ${totalSeedCost}")
    print(f"Total water cost: ${totalWaterCost}")
    print(f"Total fertilizer cost: ${totalFertilizerCost}")
    print(f"Total cost: ${totalCost}")

# Main function to run the simulation.
def main():

    # Creates variables and stores the user inputs for farm field dimensions and crop choice.
    rows = int(input("Enter farm field length (feet): "))
    cols = int(input("Enter farm field width (feet): "))
    crop = input("Seed choices:\n- Wheat\n- Corn\n- Sugarcane\n\nEnter your seed choice: ").strip().lower()
    
    # Creates the simulated farm field.
    field = createField(rows, cols)
    
    # Creates variables to store the respective costs and requirements for the chosen crop.
    seedCost = seedCostDict[crop]
    density = cropDensityDict[crop]
    waterReq = waterReqDict[crop]
    fertReq = fertilizerReqDict[crop]
    
    # Creates variables to set fixed costs for fertilizer and water.
    waterCost = 3
    fertilizerCost = 1
    
    # Plants field with crops and calculates the cost.
    totalSeedCost, totalWaterCost, totalFertilizerCost = applyResources(
        field, seedCost, waterCost, fertilizerCost, density, waterReq, fertReq)
    
    # Displays the costs.
    displayCosts(totalSeedCost, totalWaterCost, totalFertilizerCost)

# Starts the program.
main()
