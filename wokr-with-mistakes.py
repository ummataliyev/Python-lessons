age = input("Write your age: ")

try:
    age = int(age)
    print(f"You were born in {2022-age}")
except ValueError:
    print("You didn't enter an integer!")
else:
    print(f"You were born in ?{2022-age}.")
print("The program is running")
print("The program is over!")

# ZeroDivisionError
x,y = 5, 10
try:
    y/(x-5)
except ZeroDivisionError:
    print("Is not divisible by zero")

# IndexError
fruits = ['apple', 'banana', 'grape', 'avacado']
try:
    print(fruits[4])
except IndexError:
    print(f"There are only {len(fruits)} in the list!")

# KeyError
user = {'username': 'ummataliyev',
        'status': 'boss',
        'email': 'djohnummataliyev',
        'phone': '979998877'}

key = 'tel'
try:
    print(f"User {user[key]}")
except KeyError:
    print("There isn't such key exists!")
print(user['username'])

# FileNotFoundError
# filename = "elita.txt"
# try:
#     with open (filename) as f:
#        text = f.read()
# except FileNotFoundError:
#     print(f"{filename} is not exist!")

# import json
# import json
# files = ['student1.json', 'student2.json', 'student3.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             student = json.load(f)
#     except FileNotFoundError:
#         pass
#     else:
#         print(student['name'])
        
n = input("Write a integer number: ")
try:
    n = int(n)
    x = 20/n
except ValueError:
        print("You didn't write a integer number!")
except ZeroDivisionError:
    print("Is not divisible by zero")
else:
    print(f"x={x}")

while True:
    age = int(age)
    if age.isdigit():
        age = int(age)
        break
    print(f"You were born in {2022-age}")