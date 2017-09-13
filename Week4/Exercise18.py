# Chris Otto
# Week 4 - Program Exercise 18
# CPS313

# Prime Numbers List Program

# Create is_prime function
def is_prime(num):
    for count in range(2, num):
        if num % count == 0:
            return False
    return True

def main():

    print("The application will print out all numbers prime from 1 to 100.")

    for count in range (1,101):
        if(is_prime(count)):
            print(count)

main()