# Chris Otto
# Week 5 - Program Exercise 7
# CPS313

# Random number file writer

from random import randint

def main():
    num = int(input("Enter the number of random numbers to be created: "))

    outfile = open('Exercise7Output.txt', 'w')

    for count in range (0,num):
        random = randint(1,500)
        outfile.write(str(random))
        outfile.write('\n')

    outfile.close()

main()

