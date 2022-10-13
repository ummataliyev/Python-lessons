car0 = {
    "model": "lacetti", "color": "white",
    "year": 2018, "cost": "$13000",
    "km": 50000, "type": "auto"
}
car1 = {
    "model": "nexia 3", "color": "black",
    "year": 2015, "cost": "$9000",
    "km": 89000, "type": "mechanic"
}
car2 = {
    "model": "gentra", "color": "red",
    "year": "2019", "cost": "$15000",
    "km": 20000, "type": "auto"
}
cars = [car0, car1, car2]

for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['color']} color, "
          f"{car['year']}-year, {car['cost']}")

print(cars[0]["model"])

malibus = []

for n in range(10):
    new_car = {
        "model": "malibu",
        "color": None,
        "year": 2020,
        "cost": None,
        "km": 0,
        "type": "auto"
    }
    malibus.append(new_car)

for malibu in malibus[:3]:
    malibu["color"] = "red"

for malibu in malibus[3:6]:
    malibu["color"] = "black"

for malibu in malibus[6:]:
    malibu["color"] = "white"
    malibu["type"] = "mechanic"

for malibu in malibus:
    if malibu["type"] == "auto":
        malibu["cost"] = "$40000"
    else:
        malibu["cost"] = "$35000"

for malibu in malibus:
    print(malibu.values())

programmers = {
    "Muhammadali": ["python", "Golang", "js"],
    "Umid": ["html", "SQL"],
    "Suvonqul": ["php", "js"],
    "Haydar": ["Golang", "html"],
    "Lola": ["c++", "c#"]
}

for name, programs in programmers.items():
    print(f"\n{name.title()}:", end=' ')
    for prog in programs:
        print(f"{prog.upper()}", end=' ')

collagues = {
    "Umid": {"surname": "Ummataliyev",
             "birth_y": 2001,
             "programs": ["python", "SQL"]},

    "Muhammadali": {"surname": "Akbarov",
                    "birth_y": 2000,
                    "programs": ["python", "SQL", "js"]},

    "Suvonkul": {"surname": "Turdikulov",
                 "birth_y": 1984,
                 "programs": ["c++", "turbo pascal"]}
}

for name, info in collagues.items():
    print(f"\n{name.title()} {info['surname'].title()}, "
          f"was born in {info['birth_y']}-year.\n"
          f"Knows the following programming languages:")
    for prog in info["programs"]:
        print(prog.upper())

writer0 = {
    "name": "Dan Brown",
    "birth_y": 1964,
    "country": "America",
    "Book": "Origin"
}

writer1 = {
    "name": "Alisher Navoyi",
    "birth_y": 1441,
    "country": "Hirat",
    "Book": "Xamsa"
}

writer2 = {
    "name": "Elif Shafaq",
    "birth_y": 1971,
    "country": "Turkia",
    "Book": "40 rules of love"
}

writers = [writer0, writer1, writer2]
for writer in writers:
    print(f"{writer['name'].title()} was born in "
          f"{writer['birth_y']} in {writer['country']}. "
          f"The famous book is {writer['Book']}!")

films = {
    "Umid": ["Legend"],
    "Muhammadali": ["Jumong"],
    "Suvonkul": ["Lolo"],
    "Dilshod": ["Avengers"]
}

for name, films in films.items():
    print(f"\n{name.title()}'s favourite film is")
    for film in films:
        print(film)
