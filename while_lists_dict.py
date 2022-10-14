print("Please, write your close friend's name")
names = []
n = 1
while True:
    question = f"Enter your {n}-friend's name:"
    name = input(question)
    names.append(name)
    repeat = input("Do you want to add another one? (yes or no)")
    n += 1
    if repeat != "yes":
        break
print("Thank you!")
print("Your friends list:")
for name in names:
    print(name.title())

meals = []
print("What do you want to eat!")
n = 1
while True:
    question = f"What would you like for your {n}-meal?"
    meal = input(question)
    meals.append(meal)
    answer = input("Do you want to add another one? (yes or no)")
    if answer == "yes":
        n += 1
        continue
    else:
        break
print("Thank you!")
print("Your orders list:")
for meal in meals:
    print(meal.title())

print('A list of products and their prices for the "E-bozor".')
products = {}
while True:
    name = input("Write product's names please?")
    cost = input(f"Write the price of the {name.title()}:")
    products[name] = int(cost)

    answer = input("Do you want to add another info? (yes or no)")
    if answer == "yes":
        continue
    else:
        break
print("Thank you!")

for name, cost in products.items():
    print(f"The price of the {name.title()} is {cost} soums.")
