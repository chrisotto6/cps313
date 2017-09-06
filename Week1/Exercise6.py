# Chris Otto
# Week 1 - Program Exercise 6
# CPS313

# Read the purchase amount from the user, calculates the state and country tax
# returning that information to the user

purchase = float(input('Enter the purchase amount: '))

# Calculate the taxes and tax totals based on input
stateTax = purchase * 0.05
countyTax = purchase * 0.025
totalTax = stateTax + countyTax

# Find out the end price of the purchase after tax
finalPurchase = purchase + totalTax

# Display information to the user
print('Original Amount of Purchase: ', purchase)
print('State Sales Tax: ', stateTax)
print('Country Sales Tax: ', countyTax)
print('Total Sales Tax: ', totalTax)
print('Final Purchase Price: ', finalPurchase)