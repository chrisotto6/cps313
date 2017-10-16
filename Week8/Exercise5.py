# Chris Otto
# Week 8 - Program Exercise 5
# CPS313

# Alphabetic Telephone Number Translator

def main():
    number = input("Enter a telephone number: ")
    number = number.upper()
    converted = ""
    i = 0

    while i < len(number):
        if number[i] == 'A' or number[i] == 'B' or number[i] == 'C':
            converted += '2'
        elif number[i] == 'D' or number[i] == 'E' or number[i] == 'F':
            converted += '3'
        elif number[i] == 'G' or number[i] == 'H' or number[i] == 'I':
            converted += '4'
        elif number[i] == 'J' or number[i] == 'K' or number[i] == 'L':
            converted += '5'
        elif number[i] == 'M' or number[i] == 'N' or number[i] == 'O':
            converted += '6'
        elif number[i] == 'P' or number[i] == 'Q' or number[i] == 'R' or number[i] == 'S':
            converted += '7'
        elif number[i] == 'T' or number[i] == 'U' or number[i] == 'V':
            converted += '8'
        elif number[i] == 'W' or number[i] == 'X' or number[i] == 'Y' or number[i] == 'Z':
            converted += '9'
        else:
            converted += number[i]
        i += 1

    print("\nThe convertered number is:", converted)

main()