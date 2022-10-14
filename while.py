name = input("What is your name?")
question = f"Hello {name.title()}, how old are you?"
age = input(question)
age = int(age)
height = input("How tall are you?")
height = float(height)
print(f"Your height is {height}.")

number = 1
while number <= 5:
    print(number, end=' ')
    number = number + 1
print("The program is over!")

print("The program that calculates the square of an input number")
question = "Enter any number "
question += '(click "exit" to end the program): '
flag = True
while flag:
    value = input(question)
    if value == "exit":
        flag = False
    else:
        print(float(value)**2)
print("The program is over!")

print("The program that calculates the square of an input number")
question = "Enter any number "
question += '(click "exit" to end the program): '
flag = True
while flag:
    value = input(question)
    if value == "exit":
        break
    else:
        print(float(value)**2)
print("The program is over!")

flag = True
while True:
    value = str(input("How old are you?"))

    if value == "exit" or value == "quit":
        break
    age = int(value)

    if age < 3:
        cost = 0
    elif 3 <= age < 7:
        cost = 2000
    elif 7 <= age < 18:
        cost = 3000
    elif 18 <= age < 65:
        cost = 10000
    else:
        cost = 0

    if cost == 0:
        print("It's free for you to enter!")
    else:
        print(f"It is {cost} soums for you!")

print("List of the age of your close friends!")
friends = {}
while True:
    name = input("Write your friend's name:")
    age = input(f"Write {name.title()}'s age:")
    friends[name] = int(age)

    answer = input("Do you want to add another information? (yes or no)")
    if answer == "no":
        break
for name, age in friends.items():
    print(f"{name.title()} is {age} years old!")
