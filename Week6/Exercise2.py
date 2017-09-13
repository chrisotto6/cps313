# Chris Otto
# Week 6 - Program Exercise 2
# CPS313

# Lottery - Big Money

import random

def main():
    lottery = []
    num = 0
    winning = 0

    for i in range(7):
        num = random.randint(0,9)
        lottery.append(num)
        winning = (winning * 10) + num

    print("Contents of the List: ")

    for i in range(7):
        print(lottery[i])

    print("\nThe winning number is: ", winning)

main()