# Author: Conor Long
# Module 3 Lab
# An interactive program, simulating a coffee shop, calculates a receipt based on the user's order.

# Defines repeatable value used for format.
segmentSeperator = '***************************************'

# Stores total cost of items bought.
shopTotal = 0

# Prints formatting text.
print(segmentSeperator)

# Prints text
print('My Coffee and Muffin Shop')

# User inputs numbers of coffee bought.
coffeeBought = input('Number of coffees bought?\n')

# Calculates and stores the price value of coffeesBought into coffeeTotal.
coffeeTotal = int(coffeeBought) * 5

# User inputs number of teas bought.
teasBought = input('Number of teas bought?\n')

# Calculates and stores the price value of teasBought into teasTotal.
teasTotal = int(teasBought) * 2

# User inputs number of muffins bought.
muffinsBought = input('Number of muffins bought?\n')

# Calculates and stores the price value of coffeesBought into muffinsTotal.
muffinsTotal = int(muffinsBought) * 4

# User inputs number of cinnamon rolls bought.
cinnarollsBought = input('Number of cinnamon rolls bought?\n')

# Calculates and stores the price value of cinnarollsBought into cinnarollsTotal.
cinnarollsTotal = int(cinnarollsBought) * 6

# Calculates and stores the total price value of the items
shopTotal = coffeeTotal + teasTotal + muffinsTotal + cinnarollsTotal

# Prints text.
print(segmentSeperator)

# Prints text which skips a line.
print()

# Prints text.
print(segmentSeperator + '\nMy Coffee and Muffin Shop Receipt')

# If the user enters a value other than 1 for coffeeBought, a different message is printed for grammar reasons.
if coffeeBought == '1': 
    print(str(coffeeBought) + ' Coffee at $5 each: $ ' + str(coffeeTotal) + '.00')
else:
    print(str(coffeeBought) + ' Coffees at $5 each: $ ' + str(coffeeTotal) + '.00')

# If the user enters a value other than 1 for teasBought, a different message is printed for grammar reasons.
if teasBought == '1':
    print(str(teasBought) + ' Tea at $2 each: $ ' + str(teasTotal) + '.00')
else:
    print(str(teasBought) + ' Teas at $2 each: $ ' + str(teasTotal) + '.00')

# If the user enters a value other than 1 for muffinsBought, a different message is printed for grammar reasons.
if muffinsBought == '1':
    print(str(muffinsBought) + ' Muffin at $4 each: $ ' + str(muffinsTotal) + '.00')
else:
    print(str(muffinsBought) + ' Muffins at $4 each: $ ' + str(muffinsTotal) + '.00')

# If the user enters a value other than 1 for cinnarollsBought, a different message is printed for grammar reasons.
if cinnarollsBought == '1':
    print(str(cinnarollsBought) + ' Cinnamon Roll at $6 each: $ ' + str(cinnarollsTotal) + '.00')
else:
    print(str(cinnarollsBought) + ' Cinnamon Rolls at $6 each: $ ' + str(cinnarollsTotal) + '.00')

# Calculates and stores "tax" in a variable by multiplying the value stored in "shopTotal" by .06, or 6% expressed as a decimal.
tax = int(shopTotal) * .06

# Calculates and stores "actualTotal" as a float into a variable by subtracting the value stored in "tax" from the value stored in "shopTotal." 
actualTotal = float(shopTotal - tax)

# Prints text.
print(f'6% tax: $ {tax:.2f}' + '\n---------\nTotal: $ ' + f'{actualTotal:.2f}' + '\n' + segmentSeperator)

# Prints text which skips a line.
print()

# Prints text.
print(segmentSeperator + '\nThank you for your order! Come again!\n' + segmentSeperator)
