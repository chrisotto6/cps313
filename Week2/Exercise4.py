# Chris Otto
# Week 2 - Program Exercise 4
# CPS313

# Define a main function and prompt user for input
def main():
    num = int(input('Enter in a number between 1 and 10: '))

    # Validate the input is between 1 and 10 and then print the correct
    # Roman numeral based on user input
    if(num>=1 and num <= 10):
        if(num == 1):
            print("I")
        elif(num == 2):
            print("II")
        elif(num == 3):
            print("III")
        elif(num == 4):
            print("IV")
        elif(num == 5):
            print("V")
        elif(num == 6):
            print("VI")
        elif(num == 7):
            print("VII")
        elif(num == 8):
            print("VIII")
        elif(num == 9):
            print("IX")
        else:
            print("X")
    else:
        print("Error: Input outside range.")
main()