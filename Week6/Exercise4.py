# Chris Otto
# Week 6 - Program Exercise 4
# CPS313

# Number analysis program

def main():
    userInput = []

    for i in range(20):
        num = int(input("Enter one number: "))
        userInput.append(num)

    smallest = min(userInput)
    largest = max(userInput)
    total = 0

    for i in range (20):
        total += int(userInput[i])

    average = total / 20

    print("\nThe details of the input are: ")
    print("\nLowest number: ", smallest)
    print("\nHighest number: ", largest)
    print("\nTotal: ", total)
    print("\nAverage: ", average)

main()