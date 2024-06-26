# Module 4 Lab-4
# Conor Long
# 6/17/2024
# This program simulates an employee bonus calculator for businesses. It calculates individual store employee bonuses based on their store's store statistics and sales increase.

# This declares multiple variables.
monthlySales = 0  # The monthly sales amount.
storeAmount = 0  # The store bonus amount.
empAmount = 0  # The employee bonus amount.
salesIncrease = 0  # The percent of sales increase.
prompt = 'Please enter the following store statistics:'    

# A variable has an input while stores the monthly sales.
monthlySales = float(input(prompt))

# This if-elif-else statement etermines the store bonus.
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# This code gets the percent of increase in sales.
salesIncrease = float(input('Enter the percent of sales increase:'))
salesIncrease = salesIncrease / 100

# This if-elif-else statement determines the employee bonus.
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

# This code prints the bonus information.
print('The store bonus amount is $', storeAmount)
print('The employee bonus amount is $', empAmount)
if (storeAmount == 6000 ) & (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible!')
