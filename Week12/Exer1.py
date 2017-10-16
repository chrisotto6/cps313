# Chris Otto
# Week 12 - Program Exercise 1
# CPS313

# Recursive Printing

def recursive(n):
    if n > 0:
        recursive(n - 1)
        print(n)

def main():
    num = int(input('Enter a positive integer:'))
    recursive(num)

main()