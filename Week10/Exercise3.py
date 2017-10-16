# Chris Otto
# Week 10 - Program Exercise 3
# CPS313

# Personal Information Class

class Person:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone
    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_age(self, age):
        self.__age = age
    def set_phone(self, phone):
        self.__phone_number = phone
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_phone(self):
        return self.__phone_number
    def __repr__(self):
        return "\nPerson is: \nName: %s \nAddress: %s \nAge: %d \nPhone: %s"%(self.__name, self.__address, self.__age, self.__phone_number)

def main():
    person1 = Person('Chris Otto', '123 Test Way', 29, '555-555-5555')
    person2 = Person('Madalyn Otto', '123 Test Way', 28, '555-555-5556')
    person3 = Person('Wilson Otto', '123 Test Way', 5, '555-555-WOOF')

    print (person1)
    print (person2)
    print (person3)

main()