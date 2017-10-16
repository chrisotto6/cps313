# Chris Otto
# Week 10 - Program Exercise 2
# CPS313

# Car Class

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5
    def get_speed(self):
        return self.__speed

def main():
    car = Car(2017, 'Jeep Grand Cherokee')

    car.accelerate()
    print('Current speed:', car.get_speed())

    car.accelerate()
    print('Current speed:', car.get_speed())

    car.accelerate()
    print('Current speed:', car.get_speed())

    car.accelerate()
    print('Current speed:', car.get_speed())

    car.accelerate()
    print('Current speed:', car.get_speed())

    car.brake()
    print('Current speed:', car.get_speed())

    car.brake()
    print('Current speed:', car.get_speed())

    car.brake()
    print('Current speed:', car.get_speed())

    car.brake()
    print('Current speed:', car.get_speed())

    car.brake()
    print('Current speed:', car.get_speed())
main()