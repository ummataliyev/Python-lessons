with open('C:/Users/user/Desktop/python/files theme/pi.value.txt') as file:
    pi = file.read()
pi = pi.rstrip()
pi = pi.replace('\n', '')
pi = float(pi)
print(pi)

filename = 'C:/Users/user/Desktop/python/files theme/data/talabalar.txt'
with open(filename) as file:
    for line in file:
        print(line)

with open(filename) as file:
    talabalar = file.readlines()

print(talabalar)

talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)



filename = 'sapiens.txt'
name = 'Umidjon Ummataliyev'
birth_y = 2000
with open (filename, 'w') as file:
    file.write(name + '/n')
    file.write(str(birth_y)+ '/n')

import pickle

student1 = {'name': 'Umid', 'surname': 'ummataliyev', 'birth_y': 2000, 'course': 2}
student2 = {'name': 'muhammadali', 'surname': 'akbarov', 'birth_y': 2000, 'coures': 2}

with open('info.pkl', 'wb') as file:
    pickle.dump(student1, file)
    pickle.dump(student2, file)

with open('info.pkl', 'rb') as file:
    student1 = pickle.load(file)
    student2 = pickle.load(file)

print(student1)
print(student2)