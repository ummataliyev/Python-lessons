class Car:
    __num_car = 0
    """
    Car class
    """
    def __init__(self, make, model, color, year, cost):
        """
        Charactiristic of car
        """
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.cost = cost
        Car.__num_car += 1

    def __repr__(self):
        return f"Car {self.make} {self.model}"
    
    def __eq__(self, y):
        return self.cost == y.cost
    
    def __lt__(self, y):
        return self.cost < y.cost

    def __le__(self,y):
        return self.cost <= y.cost

car1 = Car("GM", "Tahoe", "Black", 2021, 10000)
car2 = Car("BMW", "x7", "Blue", 2020, 20000)

class CarDealership:
    """
    Dealership class
    """
    def __init__(self, name):
        self.name = name
        self.cars = []

    def __repr__(self):
        return f"{self.name} car dealership"
    
    def __getitem__(self, index):
        return self.cars[index]

    def __setitem__(self, index, value):
        self.cars[index]= value
        
    def add_car(self, *value):
        for car in value:
            if isinstance(car,CarDealership):
                self.cars.append(car)
            else:
                print("Please, add cars.")
    
    def __call__(self, *value):
        if value:
            for car in value:
                self.cars.append(car)
        else:
            return [car for car in self.cars]

    def __add__(self,y):
        if isinstance(y,CarDealership):
            new_dealership = CarDealership(f"{self.name} {y}")
            new_dealership.cars = self.cars + y
            return new_dealership
        elif isinstance(y,CarDealership):
            self.add_car(y)



dealership1 = CarDealership("MaxAuto")

car1 = CarDealership("GM", "Malibu", "Black", 2020, 40000)
car2 = CarDealership("BMW", "x7", "Red", 2022, 150000)
car3 = CarDealership("Mercedes", "G-class", "White", 2021, 100000)

dealership1.add_car(car1, car2, car3)

# Homework

class Student:
    """Class of student"""
    def __init__(self, name, surname, passport, birth_y, idnum, adress):
        """Characteristic of student"""
        super().__init__(name, surname, passport, birth_y)
        self.idnum = idnum
        self.course = 1
        self.adress = adress

    def __repr__(self):
        return f"{self.name} {self.surname}"

()