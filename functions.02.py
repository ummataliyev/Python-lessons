def car_info(make, modle, color, box, year, cost=None):
    car = {
        'company': make,
        'model': modle,
        'color': color,
        'box': box,
        'year': year,
        'cost': cost
    }
    return car

car1 = car_info("GM", "Malibu", "black", "automat", 2018)
car2 = car_info("GM", "Gentra", "white", "mechanic", 2016, 15000)
cars = [car1, car2]

print("List of available cars on the online market:")
print(cars)

# Homework

def multiply(*numbers):
    multiplication = 1
    for son in numbers:
        multiplication *= son
    return multiplication

def summa(*numbers):
    """A function that calculates the sum of the input numbers"""
    total = 0
    for number in numbers:
        total += number
    return total

print(summa(1,2))
print(summa(1,2,3,4,5))
print(summa(4,5,6,7))

def summa(x,y, *numbers):
    """A function that calculates the sum of the input numbers"""
    return x+y+sum(numbers)

print(summa(1,2,3,4,5))
print(summa(4,5,6,7))
print(summa(2,3))

def car_info(company, model, **infomations):
    """Function that returns the vehicle data in dictionary form"""
    infomations["company"] = company
    infomations["model"] = model
    return infomations

car1 = car_info("GM", "Malibu", color = "black", year=2018)
car2 = car_info("Kia", "K5", color = "red", cost = 35000, year = 2020)
cars = [car1, car2]
print(cars)
