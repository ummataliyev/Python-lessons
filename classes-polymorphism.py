from ast import Delete
from os import remove


class Person:
    """Information about person"""
    def __init__(self, name, surname, passport, birth_y):
        """Characteristic of person"""
        self.name = name
        self.surname = surname
        self.passport = passport
        self.birth_y = birth_y

    def get_info(self):
        """Information about person"""
        info = f"{self.name} {self.surname}."
        info += f"Passport: {self.passport}, {self.birth_y}-year"
        return info
    
    def age(self, year):
        return year - self.birth_y
    
class Student(Person):
    """Class of student"""
    def __init__(self, name, surname, passport, birth_y, idnum, adress):
        """Characteristic of student"""
        super().__init__(name, surname, passport, birth_y)
        self.idnum = idnum
        self.course = 1
        self.adress = adress

    def get_id(self):
        """ID number of student"""
        return self.idnum

    def get_course(self):
        """Course of student"""
        return self.course
    
    def get_info(self):
        """Information about course"""
        info = f"{self.name} {self.surname}. "
        info += f"{self.get_course()}-course. ID number {self.idnum}"
        return info

class Adress:
    """Class for save adresses"""
    def __init__(self, home, street, district, region):
        """Characteristic of adress"""
        self.home = home
        self.street = street
        self.district = district
        self.region = region

    def get_adress(self):
        """See adress"""
        adress = f"{self.region} region, {self.district} district, "
        adress += f"{self.street} street, {self.home}-home"
        return adress

student1_adress = Adress(12, "Timesquare", "Brooklyn", "New York")
student1 = Student("Umidjon", "Ummataliyev", "AB7877707", 2000, "UZ8880888", student1_adress)

print(student1.adress.get_adress())
print(student1_adress.district)

# Homework

class Student:
    """Information about student"""
    def __init__(self, name: str, surname: str, birth_y: str):
        """
        Characteristic of student.
        """
        self.name = name
        self.surname = surname
        self.birth_y = birth_y
        self.enrolled_courses = []

    def enroll_in_sub(self, subject: str):
        """
        Courses which is students enrolled.
        """
        self.enrolled_courses.append(subject)


class Subjects(Student):
    """
    Class for subjects
    """
    def __init__(self, history, math, english):
        super().__init__(history,math, english)
        self.history = history
        self.math = math
        self.english = english

    def remove_sub(self, subject: str):
        self.subject = subject
        for subject in self.enrolled_courses:
            if subject in self.enrolled_courses:
                list.remove(subject)
            else:
                print("There isn't no such subject in list!")

