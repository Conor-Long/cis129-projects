# Module 5 Lab: Your Name
# Conor Long
# 6/19/2024
# This program tracks the collection of a grocery store's bottle recycling over 1 week periods. It calculates and prints the total bottles collected as well as the total payout from selling them to recycling.

# Step 1: Declare variables below 
NBR_OF_DAYS = 7
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = 'y'

# Step 1: Declare variables below 
NBR_OF_DAYS = 7
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = 'y'
	
# Step 2: Loop to run program again
while counter <= NBR_OF_DAYS:
    for todayBottles in range(7):
        todayBottles = input('Enter number of bottles for day #' + str(counter) + ': ')
        totalBottles += int(todayBottles)
        counter += 1

    # Step 3: Code to set value of variables 
    totalPayout = 0
    PAYOUT_PER_BOTTLE = .10
    totalPayout = totalBottles * PAYOUT_PER_BOTTLE
    print('\nThe total number of bottles collected is ' + str(totalBottles) + f'\nThe total paid out is: ${totalPayout:.2f}')
    print('\nDo you want to enter another week\'s worth of data?')
    keepGoing = input('(Enter y or n): ')
    print()

    # Restarts the loop if keepGoing equals 'y'
    if keepGoing == 'y':
        counter = 1
        continue
    else:
        break	



