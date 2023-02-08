#Files

file = open("word.txt")
while True:
    content = file.read(10)
    if content == "":
        break                               
    print(content, end="")


file.close()

files = []

for i in range(1000):
    with open(f"trash/{i}.txt", "w") as file:
        files.append(file)

