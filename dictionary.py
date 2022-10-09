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
