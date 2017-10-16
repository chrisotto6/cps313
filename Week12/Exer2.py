# Chris Otto
# Week 12 - Program Exercise 2
# CPS313

# Recursive Multiplication

def recursive(x, y):
    if (y == 0):
        return 0
    return x + recursive(x, y - 1)


def main():
    print('Recursive multiplication....')
    num1 = int(input('Enter in the first number:'))
    num2 = int(input('Enter in the second number:'))

    print(recursive(num1, num2))


main()
