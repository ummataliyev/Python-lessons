number = int(input("Enter an even number:"))
if number > 0:
    print("Thanks")
if number != 0:
    print("it isn't an even number!")

age = int(input("How old are you?"))
if age < 4 and age > 60:
    print("It is free for you!")
if age < 18:
    print("It is 10000 thousand soums for you1")
if age > 18:
    print("It is 20000 thousand soums for you!")

a = int(input("Enter the first  number you want:"))
b = int(input("Enter the second number you want"))
if a > b:
    print(f"{a} > {b}")
if a < b:
    print(f"{a} < {b}")
if a == b:
    print(f"{a} = {b}")

products = ["sugar", "salt", "apple", "banana", "tea", "fanta",
            "coca cola", "ananas", "chocolate", "juice"]
basket = []
for n in range(5):
    basket.append(input(f"Add product {n+1} to basket"))
yes_products = []
not_products = []
for product in basket:
    if products in products:
        yes_products.append(products)
    else:
        not_products.append(products)
if not_products:
    print("Our store doesn't have theese products!")
    for products in not_products:
        print("Product")
else:
    print("We have all the products you asked for in our store")
