student = {
    "name": "Umidjon",
    "surname": "Ummataliyev",
    "age": 22,
    "faculty": "oilandgas",
    "course": 4
}
for key, value in student.items():
    print(f"Key: {key}")
    print(f"Value: {value}")

    phones = {
        "Umid": "iPhone 14pro max",
        "Javokhir": "xiaomi note8",
        "Rakhmatillo": "iPhone 14pro max",
        "Shavkat": "iPhone 5S"
    }
for k, q in phones.items():
    print(f"{k.title()}ning telefoni {q}")

products = {
    "apple": 10000,
    "banana": 20000,
    "grape": 15000,
    "avacado": 50000
    }
print("Do'kondagi mahsulotlar:")
for product in products.keys():
    print(product.title())

market = ["banana", "grape", "fish", "bread"]
for product in products:
    if product in market:
        print(f"{product.title()} {products[product]} so'm")

for smth in market:
    if smth not in products:
        print(f"Please, bring {smth} to your shop")

print("Products in our store:")
for product in sorted(products):
    print(product.title())

print(phones.values())
print("Users use thev theese phones:")
for phone in phones.values():
    print(phone.title())

print("Users use the theese phones:")
for phone in set(phones.values()):
    print(phone)

toys = {"ball", "car", "lapm", "bear", "car"}
print(toys)
