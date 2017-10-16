# Chris Otto
# Week 11 - Program Exercise 1
# CPS313

# Employee and ProductionWorker Classes

class Employee:
    def __init__(self,name,number):
        self.__name = name
        self.__number = number
    def set_name(self,name):
        self.__name = name
    def set_number(self,number):
        self.__number = number
    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number

class ProductionWorker(Employee):
    def __init__(self,name,number,shift,pay):
        Employee.__init__(self,name,number)
        self.__shift = shift
        self.__pay = pay
    def set_shift(self,shift):
        self.__shift = shift
    def set_pay(self,pay):
        self.__pay = pay
    def get_shift(self):
        return self.__shift
    def get_pay(self):
        return self.__pay

def main():
    print('Create a new employee...')
    name = input('\nEnter name:')
    number = input('Enter number:')
    shift = input('Enter shift:')
    pay = input('Enter pay:')

    worker = ProductionWorker(name, number, shift,pay)

    print('New production worker is...')
    print('\nName:', worker.get_name())
    print('Number:', worker.get_number())
    print('Shift:', worker.get_shift())
    print('Pay:', worker.get_pay())

main()