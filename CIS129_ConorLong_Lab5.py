# Lab 5 The Bottle Return Program

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
        print('Enter number of bottles returned Day ' + str(counter) + ':')
        todayBottles = input()
        print('Day ' + str(counter) + ' payout is: $' + str(int(todayBottles) * .10))
        print('Day ' + str(counter) + ' bottles added to the total count is : ' + str(todayBottles))
        totalBottles += int(todayBottles)
        counter += 1
      	# Step 3: Code to set value of variables 
    totalPayout = 0
    PAYOUT_PER_BOTTLE = .10
    totalPayout = totalBottles * PAYOUT_PER_BOTTLE
    print('The total number of bottles is: ' + str(totalBottles) + f'\nTotal Payout: ${totalPayout:.2f}')
    print('Do you want to enter another week\'s worth of data?')
    print('(Enter y or n)')
    keepGoing = input()
    if keepGoing == 'y':
        counter = 1
        continue
    else:
        break	

