fruits = ["apple", "grape", "banana", "avacado"]
costs = [100, 200, 300, 400]
numbers = ["one", "two", "three", "four", "five"]
fruits.append("watermelon ")
print(fruits)
fruits.insert(0, "grape")
print(fruits)
fruits.insert(3, "peach")
print(fruits)

cars = []
cars.append("lacetti")
cars.append("naxia")
cars.append("malibu")
print(cars)
del cars[0]
print(cars)
cars.insert(0, "lacetti")
print(cars)
cars.remove("malibu")
print(cars)

animals = ["cat", "cow", "dog", "horse", "cat"]
print(animals)
animals.remove("cat")
print(animals)

cars = ["bmw", "audi", "amg", "general motors", "volvo", "mustang"]
cars.sort()
print(cars)
cars = ["bmw", "audi", "amg", "general motors", "volvo", "mustang"]
cars.sort(reverse=True)
print(cars)
cars = ["bmw", "audi", "amg", "general motors", "volvo", "mustang"]
sorted(cars)
print(sorted(cars))

numbers = [7, 8, 9, -5, -7, -3]
print(sorted(numbers))
numbers = [7, 8, 9, -5, -7, -3]
numbers.sort()
numbers.sort(reverse=True)
print(numbers)

len(cars)
print(len(cars))
numbers = list(range(0, 10))
print(numbers)
odd_numbers = list(range(1, 30, 2))
print(odd_numbers)
even_numbers = list(range(0, 30, 2))
print(even_numbers)
count = list(range(0, 100, 10))
print(count)
numbers = [10, 20, 30, 40, 50, 60]
max_value = max(numbers)
print(max_value)
numbers = [10, 20, 30, 40, 50, 60]
min_value = min(numbers)
print(min_value)
numbers = [10, 20, 30, 40, 50, 60]
sum_numbers = sum(numbers)
print(sum_numbers)

cars = ["bmw", "audi", "amg", "general motors", "volvo", "mustang"]
print(cars[0:3])
cars = ["bmw", "audi", "amg", "general motors", "volvo", "mustang"]
print(cars[2:4])
cars = ["bmw", "audi", "amg", "general motors", "volvo", "mustang"]
print(cars[1:])
cars = ["bmw", "audi", "amg", "general motors", "volvo", "mustang"]
my_cars = cars[:]
my_cars.remove("volvo")
print(cars)
print(my_cars)
cars = ("bmw", "audi", "amg", "general motors", "volvo", "mustang")
print(cars)

# HOMEWOKR
country = ["Uzb", "USA", "Dubai", "Germany", "Spain", "Europe"]
print(country)
print(len(country))
print(sorted(country))
print(sorted(country, reverse=True))
country = ["Uzb", "USA", "Dubai", "Germany", "Spain", "Europe"]
country.sort(reverse=True)
print(country)
numbers = list(range(120, 1200, 2))
print(numbers)
print(sum(numbers))
