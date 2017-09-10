# Chris Otto
# Week 3 - Program Exercise 6
# CPS313

# Create a program that calculates the factorial of a number

def main():
    num=int(input('Enter the number for the factorial calculation: '))

    tracker = 1

    for num in range (1,num + 1):
        tracker = tracker * num

    print('\nThe factorial of your number is: ', tracker)
main()