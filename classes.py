x = 10
print(type(x))
matn = "salom"
print(type(matn))
print(matn.upper())

def salom():
    print("Assalomu alekum")

class Student:
    def __init__(self,name,surname,birth_y):
        self.name = name
        self.surname = surname
        self.birth_y = birth_y
    def get_name(self):
        return self.name
    
    def get_age(self,year):
        return year - self.birth_y
        
    def introduce(self):
        print(f"My name is {self.name} {self.surname}, and I was bor in {self.birth_y}.")

student1 = Student("Umidjon", "Ummataliyev", 2000)
student2 = Student("Muhammadali", "Akbarov", 2000)
student3 = Student("Azizbek", "Tojimahammatov", 2000)

print(student1.get_name())
print(student1.get_age(2021))

# Homework

class User:
    """User class"""
    def __init__(self, name, surname, username, gmail):
        self.name = name
        self.surname = surname
        self.username = username
        self.gmail = gmail

    def get_info(self):
        """A function gives information about users"""
        return f"User:\nFull name:{self.name.upper()} {self.surname.upper()}\nusername:{self.username}\ngmail:{self.gmail}"

user1 = User("umidjon", "ummataliyev", "the_elita", "djohnummataliyev")
print(user1.get_info())