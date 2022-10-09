guests = ["Ali", "Shaxdias", "Umid", "Fayz", "Sherqo'zi"]
print(guests[1])
for dear in guests:
    print("Hello", dear)
    guests = ["Ali", "Shaxdias", "Umid", "Fayz", "Sherqo'zi"]
for dear in guests:
        print(f"Hurmatli {dear},")
        print("Sizni 20-mart kuni nahorgi oshga taklif qilamiz.")
        print("Hurmat bilan, Ummataliyevlar oilasi!\n")
numbers = list(range(1,11))
for number in numbers:
    print(f"The square of the {number} is equals to {number**2}")
numbers = list(range(11))
square_of_numbers = []
for number in numbers:
    square_of_numbers.append(number**2)
    print(numbers)
    print(square_of_numbers)
friends = []
print("Write five your best friend's name:")
for n in range (5):
    friends.append(input(f" {n+1}- write your friends name:"))
    print(friends)