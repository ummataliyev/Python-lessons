class Person:
    """Information about person"""
    def __init__(self, name, surname, passport, birth_y):
        """Characteristic of person"""
        self.name = name
        self.surname = surname
        self.passport = passport
        self.birth_y = birth_y

class Student(Person):
    """Class of student"""
    def __init__(self, name, surname, passport, birth_y, idnum, adress):
        """Characteristic of student"""
        super().__init__(name, surname, passport, birth_y)
        self.idnum = idnum
        self.course = 1
        self.adress = adress
