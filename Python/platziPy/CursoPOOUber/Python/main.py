from car import Car
from account import Account


if __name__ =='__main__':

    car = Car("AMS345", Account("Juanito Perez", "12345"))
    print(vars(car))
    print(vars(car.driver))

    car2 = Car("TUW456", Account("Cecilia Martinez", "6789"))
    print(vars(car2))
    print(vars(car2.driver))