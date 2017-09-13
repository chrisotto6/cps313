# Chris Otto
# Week 5 - Program Exercise 8
# CPS313

def main():

    infile = open('Exercise7Output.txt', 'r')
    sum = 0
    count = 0

    for line in infile:
        num = int(line)

        print("Number: " + format(num,'.0f'))
        sum += num
        count += 1

    infile.close()
    print("\nSum of all numbers: ", sum)
    print("Count of all numbers: ", count)

main()