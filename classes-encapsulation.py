from uuid import uuid4
class Car:
    """
    Car class
    """
    __num_car = 0
    def __init__(self, make, model, color, year, cost, km = 0):
        """
        Charactiristic of car
        """
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.cost = cost
        self.__km = km
        self.__id = uuid4()
        Car.__num_car += 1
    
    @classmethod
    def get_num_car(cls):
        return cls.__num_car

    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id

    def add_km(self, km):
        """
        Add km to km of car
        """
        if km >= 0:
            self.__km += km
        else:
            print("The mileage of the car cannot be reduced!")
        

car1 = Car("GM", "Malibu", "Black", 2020, 40000, 1000)
car2 = Car("BMW", "x7", "Red", 2022, 150000, 100)
car3 = Car("Mercedes", "G-class", "White", 2021, 100000, 5000)

print(car1.get_num_car())
