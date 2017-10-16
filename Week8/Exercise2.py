# Chris Otto
# Week 8 - Program Exercise 2
# CPS313

# Sum of Digits in a String

def main():
    string = input("Enter a number: ")
    length = len(string)
    sum = 0
    i = 0

    while i < length:
        if string[i].isdigit():
            sum += int(string[i])
        else:
            print(string[i], "is not a number.")
            break
        i += 1

    if i == length:
        print("The sum of the string entered is: ", sum)
    else:
        print("The string entered had non-number characters. Invalid.")
main()