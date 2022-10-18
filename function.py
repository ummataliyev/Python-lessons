def say_hello(name):
    """Greeting function"""
    print(f"Assalomu alaykum {name.title()}! ")

say_hello('Umid')
say_hello('Muhammadali')

print(say_hello.__doc__)

def count_age(name, birth_y):
    """A program that calculates the user's age"""
    print(f"{name.title()} is {2020-birth_y} years old.")

count_age('Umid', 2000)
count_age('Muhammadali', 2000)

def count_age(birht_y, now=2021):
    """A program calculates the user's age from the year of birth"""
    print(f"You are {now-birht_y} years old!")

count_age(2000)

def full_name(name, surname, fathers_name=''):
    """A function that returns a full name"""
    if fathers_name:
        full_name = f"f{name} {fathers_name} {surname}"
    else:
        full_name = f"{name} {surname}"
    return full_name.title()

student1 = full_name("umidjon", "ummataliyev")
student2 = full_name("umidjon", "ummataliyev", "bakhramovich")

print(f"Students who did not attend class: {student1} and {student2}")

def intermediate(min,max):
    numbers = []
    while min<max:
        numbers.append(min)
        min += 1
    return numbers

print(intermediate(0,10))
print(intermediate(10,20))

number = intermediate(150,200)
print(number)

print("List of cars on our site:")
cars = []
while True:
    print("\nEnter the following informations", end='')
    company = input("Manafatcturer: ")
    model = input("model: ")
    color = input("color: ")
    _type = input("type: ")
    year = input("year of manufacture: ")
    cost = int(input(("cost: ")))
    cars.append([company, model, color, _type, year, cost,])
    answer = input("Do you want to add another information? (yes/no): ")
    if answer == 'no':
        break
    
print(cars)
print("Tha automobiles on our site:")
for car in cars:
    if car[5]:
        cost = car[5]
    else:
        cost = 'not defained'
    print(f"{car['color'].title()} {car['model'].title()}, {'_type'} type. Cost: {'cost'}")

from module import car_info, info_print

car1 = car_info("GM", "Malibu", "Black", "Auto", 2020, 40000)
info_print(car1)

import math

x = 400
print(math.sqrt(x))
print(math.pow(5,3))
print(math.pi)
print(math.log2(8))
print(math.log10(100) )

import random as r

number = r.randint(0,100)
print(number)

names = ['Umid', 'Muhammadali', 'Aziz', 'Suvonqul']
name = r.choice(names)
print(name)
print(r.choice(name))

x = list(range(0,51,5))
print(x)
print(r.choice(x))

x = list(range(11))
print(x)
r.shuffle(x)
print(x)