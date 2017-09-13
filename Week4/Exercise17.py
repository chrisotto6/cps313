# Chris Otto
# Week 4 - Program Exercise 17
# CPS313

# Prime Numbers Program

# Create is_prime function
def is_prime(num):

    for count in range(2, num):
        if num % count == 0:
            return False
    return True

def main():
    num = 0

    while num < 2:
        num = int(input("Enter a number to see if it is prime (no 1's or 0's): "))
        if (num == 1 or num == 0):
            print("0 and 1 are not valid inputs; they are neither prime or composite.")

    if (is_prime(num)):
        print("The number:", num, "is prime.")
    else:
        print("The number:", num, "is non-prime.")


main()