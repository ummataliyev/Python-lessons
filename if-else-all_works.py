cars = ["audi", "bmw", "chevrolet", "kia", "hyundai"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
name = input("What is you name?\n>>>")
if name.lower() != "ali":
    print(f"Sorry, {name.title()} we are waiting Ali.")
else:
    print("Hello, Ali")
answers = str(input("12x6 nechiga teng?>>>"))
if answers != 72:
    print("Javob xato")
age = int(input("How old are you?>>>"))
if age >= 18:
    print("You are welcome!")
else:
    print("Access isn't possible")
login = input("Choose new login please:")
if len(login) < 5:
    print("Login should be more than five symbols!")
year = int(input("Enter your birth year:"))
if 2020 - year < 18:
    print(f"Your are {year} ")
    print("Acces isn't possible!")
else:
    print("You are welcome!")
x, y = 25, 50
print("x,y") if x > y else print("x<y")

number = 50
if number < 0:
    print("A negative number")
else:
    print("A positive number")
age = int(input("How old are you?"))
if age < 4:
    print("Entrance to you if free!")
elif age <= 12:
    print("Entrance to you is 5000 thousand soums!")
else:
    print("Entrance to you is 10000 thousand soums!")
age = int(input("How are old you?"))
if age <= 4:
    cost = 0
elif age <= 12:
    cost = 5000
elif age <= 14:
    cost = 8000
elif age <= 20:
    cost = 10000
print(f"Enterence to you is {cost} thousand soums!")
day = input("What day is today?>>>")
if day.lower() == "Saturday" or day.lower() == "Sunday":
    print("Today is a off day")
else:
    print("Today is work day!")
day = input("What day is today?>>>")
temperature = float(input("What is the temperature today?>>>"))

if day.lower() == "saturday" and temperature > 30:
    print("Let's go to swim!")
elif day.lower() == "Sunday" and temperature < 30:
    print("We rest at home!")

cost = 15000
tea = True
salad = False
if tea and salad:
    cost = cost + 10000
elif tea or salad:
    cost = cost + 5000
    print(f"Total price is {cost}")
cost = 15000
tea = True
salad = False
bread = True
juice = True
mix_salad = 1
if tea:
    print("The customer bought tea.")
    cost = cost + 3000
if salad:
    print("The customer bought salad.")
    cost = cost + 5000
if bread:
    print("The customer bought bread.")
    cost = cost + 2000
if juice:
    print("The customer bought juice.")
meal = input("What food do you order?")
if meal.lower() in meal:
    print("Order received")
else:
    print("Order was not received")
menu = ["osh", "kebab", "norin", "somsa"]
orders = ["osh", "somsa", "manti", "shashlik"]
for meal in orders:
    if meal in menu:
        print(f"There are {meal} in menu")
    else:
        print(f"Sorry, there isnm't {meal} in menu")
if orders:
    print(f"In menu has {len(orders)}")
