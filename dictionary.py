cars = {
    "model": "ferrari",
    "color": "red"
}

print(cars["model"])
print(cars["color"])

en_uz = {
    "apple": "olma",
    "banana": "banan",
    "apricot": "o'rik"
}

print(en_uz["apple"])

fruits = {
    "apple": 10000,
    "watermelon": 8000,
    "grape": 5000
}

fruit = fruits.get("apple")

print(f"The price of apple {fruit} soums")

fruit = fruits.get("grape")

print(f"The price of grape {fruit} soums")

student_0 = {
    "name": "murod olimov",
    "age": 20,
    "birth": 2000
}

name = student_0.get("name")
age = student_0.get("age")
birth = student_0.get("birth")

print(f"About a student {name.title()} \n{age} \n{birth}")

student_0["course"] = 4
student_0["faculty"] = "history"
student_0["name"] = "Suvonqul"
student_1 = {}
student_1["name"] = "qobil rasulov"
student_1["course"] = 3
student_1["age"] = 20

print(f"Student {student_1['name'].title()} {student_1['course']} course")

phones = {
    "djohn": "iPhone XS max",
    "james": "GalaxyS9",
    "will": "xiaomi 11pro",
    "ben": "nokia 3310",
    "efe": "pixel 3x1"
}
phone = phones.get("djohn", "Bunday ism mavjud emas")
print(phone)
fruit = en_uz.get("banana", "There isn't that fruit!")
print(fruit)

father = {
    "name": "Bakhromjon",
    "surname": "Yakubov",
    "birth": 1977
}
name = father["name"].title()
surname = father["surname"].title()
birth = father["birth"]

print(f"My father's {name} {surname}. He was born in {birth} in Andijan")

meals = {
    "father": "palov",
    "mother": "norin",
    "sister": "manti"
}
meal = meals["father"]
print(f"My father likes {meal}")

dictionary = {
    "integer": "son",
    "string": "matn",
    "float": "10 lik son",
    "title()": "bosh harf"
}

smth = str(input("What do you want to ask?"))
if smth.lower() in dictionary:
    print(f"Translation of this {dictionary.get(smth)}")
else:
    print("Sorry, error 404 not found")

dictionary = {
    "apple": "olma",
    "banana": "banan",
    "heart": "yurak",
    "car": "moshina",
    "phone": "telefon",
    "pen": "ruchka",
    "pencil": "qalam",
    "fan": "ventilyator",
    "air condition": "konditsioner",
    "box": "quti"
}

for word, translation in dictionary.items():
    print(f"Key: {word.title()}")
    print(f"Value: {translation}")

counrties = {
    "Uzbekistan": "Tashkent",
    "America": "Washignton",
    "Russia Federation": "Moscow",
    "China": "Pekin",
    "Germany": "Berlin",
    "France": "Paris"
}
print("World countries:")
for country in sorted(counrties):
    print(country.upper())

print("Captilas of countries:")
for capital in sorted(counrties.values()):
    print(capital.title())

country = str(input("What country would you like to know the capital of?"))
country = country.title()
capital = counrties.get(country)
if capital is None:
    print("Sorry, we don't have any information about it!")
else:
    print(f"The capital of {country.upper()} is the {capital.title()}.")

menu = {
    "osh": 15000,
    "norin": 25000,
    "qazi": 6000,
    "grill": 35000,
    "somsa": 5000,
}

print("Please, order three dishes:")
orders = []
for n in range(3):
    orders.append(input(f"{n+1}-meal:").lower())

for order in orders:
    if order in menu:
        print(f"{order.title()} is {menu[order]} soum.")
    else:
        print(f"Sorry, we don't have a {order}.")
