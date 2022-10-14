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
