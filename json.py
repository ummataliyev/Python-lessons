import json

from pprint import pprint

x = 10
x_json = json.dumps(x)

y = 5.5
y_json = json.dumps(y)

m = True
m_json = json.dumps(m)

sonlar = (12, 45, 23, 67)
sonlar_json = json.dumps(sonlar)


bemor = {
    "ism": "Alijon Valiyev",
    "yosh": 30,
    "oila": True,
    "farzandlar": ("Ahmad", "Bonu"),
    "allergiya": None,
    "dorilar": [
        {"nomi": "Analgin", "miqdori": 0.5},
        {"nomi": "Panadol", "miqdori": 1.2},
    ],
}

bemor_json = json.dumps(bemor)
pprint(bemor_json)

with open("sonlar.json", "w") as f:
    json.dump(sonlar, f)

bemor2 = json.loads(bemor_json)

filename = "bemor.json"
with open(filename) as f:
    bemor = json.load(f)

print(type(bemor))

# Homework

# 1
data = {"Model": "Malibu", "Color": "Black", "Year": 2020, "Cost": 105000}
data_json = json.dumps(data, indent=4)

# 2
student_json = """{"name": "Umidjon", "surname": "Ummataliyev", "birth_y": 2000}"""
student = json.loads(student_json)

print(f"{student['name']} {student['surname']}")

