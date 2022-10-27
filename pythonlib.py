# import datetime as dt
# from fileinput import filename
# import json
# import math
# from pprint import pprint
# import requests
import re
from uzwords import words

# # hozir = dt.datetime.now()
# # bugun = dt.date.today()
# # ertaga = dt.date(2022, 3, 10)
# # vaqtHozir = hozir.time()
# # print(hozir.time())
# # print(bugun)
# # print(f"Tomorrow:{ertaga}")
# # print(vaqtHozir)

# # bugun = dt.date.today()
# # ramazan = dt.date(2023,3,10)
# # farq = ramazan - bugun 
# # print(farq.days)

# # hozir = dt.datetime.now()
# # futbol = dt.datetime(2022, 11, 10, 23, 45, 00)
# # farq = futbol - hozir
# # sekundlar = farq.seconds
# # minutlar = int(sekundlar/60)
# # soatlar = int(minutlar/60)
# # print(f"Futbo'l boshlanishiga {farq.days} kunu {soatlar} soat qoldi")

# PI = math.pi
# E = math.e
# print(PI)
# print(E)

# # triganometriya
# math.sin(math.pi/2)
# math.cos(0)
# math.tan(PI)

# # radianlar va burchaklar o'rtasida konvertasiya
# print(math.degrees(math.pi/2))
# print(math.radians(90))

# # logarifmlar
# math.log(5)
# math.log(100)

# # sonlarni yaxlitlash
# x = 4.6
# print(math.ceil(x))
# print(math.floor(x))
# print(round(x))

# # kvadrat ildiz
# x = 81
# math.sqrt(x)
# print(math.sqrt(x))

# # darajaga ko'tarish
# math.pow(x, 3) # x ning kubi
# math.pow(x, 5) # x ning 5-darajasi
# math.pow(x, 1/3) # x dan kub ildiz

# print(math.pow(x, 3))
# print(math.pow(x, 1/3))

# # filename = 'bemor.json'
# with open (filename) as f:
#     bemor = json.load(f)

# pprint(bemor)

# r = requests.get('http://anvarnarz.github.com')

# pprint(r.json())
# word1 = "темир"
# word2 = "томир"
# word3 = "тулпор"

# andoza = "^т...р$"

# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))

# andoza = "^т...р$"
# matches = []
# for word in words:
#     if re.match(andoza, word):
#         matches.append(word)
# print(matches)