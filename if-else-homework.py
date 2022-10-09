# Homework
new_cars = ["toyota", "mazda", "hyundai", "gm", "kia"]
for car in new_cars:
    if car == "gm":
        print(car.upper())
else:
    print(car.title())
user_name = str(input("What is your name?>>>"))
if user_name == "Admin":
    print("Assalamu alaikum! Admin. Do you want to check user's name? ")
else:
    print(f"Assalamu alaikum! {user_name}")
a = int(input("Write your the first number: "))
b = int(input("Write your the second number: "))
if a == b:
    print(f"{a} equals to{b}")
else:
    print(f"{a} don't equal to {b}")
number = int(input("Write a number:"))
if number > 0:
    print(f"{number} is a plus")
else:
    print(f"{number} is minus")
number = int(input("Write a number please"))
if number < 0:
    print("it is negative number")
else:
    print("It is a positive number")
names = ["Umidjon", "Muhammadali", "Lily", "Sofia", "Moonlight"]
n = len(names)
for name in names:
    print(f"Hello {name}")
print(f"kod {n} marta aylandi")
numbers = list(range(10, 100))
for number in numbers:
    print(number ** 3)
films = []
print("Write your five favourite film?:")
for n in range(5):
    films.append(input(f" {n+1} - write your next film:"))
    print(films)
n_people = int(input("How many people do you meet today? :"))
names = []
for name in range(n_people):
    name.append(input(f"{n+1}-who were they? :"))
print(names)
users = ["djohngreat", "muhammadali1717", "sapiens", "elita", "efe"]
login = input("Write a new login:")
if login in users:
    print("Login busy, choose a new login!")
else:
    print("You are welcome!")
number = int(input("Please, write a number:"))
for n in range(2, 11):
    if not (number % n):
        print(f"{number} is divisible by {n} without a remainder ")
