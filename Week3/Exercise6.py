# Chris Otto
# Week 3 - Program Exercise 6
# CPS313

# Program to convert Celsius to Fahrenheit table

def main():
    celsius = 0
    print('Celsius\t\t\t\tFahrenheit')
    print('______________________________________')

    for celsius in range (0,21):
        fahrenheit = (9.0/5.0) * celsius + 32
        print(celsius,'\t\t\t\t\t',fahrenheit)
main()