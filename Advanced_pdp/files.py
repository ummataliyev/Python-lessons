import json

#Files

# file = open("word.txt")
# while True:
#     content = file.read(10)
#     if content == "":
#         break                               
#     print(content, end="")


# file.close()

# files = []

# for i in range(1000):
#     with open(f"trash/{i}.txt", "w") as file:
#         files.append(file)

# #XMl
# """
# <document>
#     <key>Value</key>
#     <name>Value</name>
# </document
# """

# #JSON
# """
# {
#     "key": "value",
#     "name": "John",
#     "job": "programmer"
# }
# """

# #CSV
# """
# key, name, job
# value, John, programmer
# value2, Bob, designer
# """


dictionary = {
    "key": "value",
    "name": "John",
    "job": "programmer"
}

content = json.dumps(dictionary)
with open("file.json", "w") as file:
    file.write(content)

with open("file.json", "r") as file:
    dictionary = json.load(file)
    print(type(dictionary))
