from types import FunctionType

class Student:
    """We create a class named student"""

    def __init__(self, name, surname, birth_y):
        """Characteristics of the student"""
        self.name = name
        self.surname = surname
        self.birth_y = birth_y
        self.course = 1

    def set_course(self, new_course):
        """Method that renews the student's course"""
        self.course = new_course

    def update_course(self):
        """Method that multiplies the student's stage by bit"""
        self.course += 1

    def get_info(self):
        """Infomation about student"""
        return f"{self.name} {self.surname}. {self.course}-course"

    def get_name(self):
        """Returns the student's name"""
        return self.name

    def get_lastname(self):
        """Returns the student's surname"""
        return self.surname

    def get_fullname(self):
        """Returns the student's fullname"""
        return f"{self.name} {self.surname}"

    def get_age(self, year):
        """Returns the student's age"""
        return year - self.birth_y

class Subject():
    def __init__(self,name):
        self.name = name
        self. num_of_students = 0
        self.students = []

    def add_student(self,student):
        """Adding students to science"""
        self.students.append(student)
        self.num_of_students += 1
    
    def get_name(self):
        """Name of subject"""
        return self.name
    
    def get_students(self):
        """Information about students enrolled in science"""
        return [student.get_info() for student in self.students]

    def get_students_num(self):
        """Number of students enrolled in the subject"""
        return self.students_num

    def see_methods(Student):
        return [x for x, y in Student.__dict__.items() if type(y) == FunctionType]


math = Subject("Higher math")
student1 = Student("Umidjon", "Ummataliyev", 2000)
student2 = Student("Akbarov", "Muhammadali", 2000)
student3 = Student("Tojimahammatov", "Azizbek", 2000)

math.add_student(student1)
math.add_student(student2)
math.add_student(student3)

print(math.num_of_students)

print(math.students)

math_students = math.get_students()

# Homework

class Auto_mobile():
    """Automobiles"""

    def __init__(self,model,color,box,cost):
        """Characteristics of the automobile"""
        self.model = model
        self.color = color
        self.box = box
        self.cost = cost
        self.km = 0

    def get_model(self):
        return self.model
    
    def get_color(self):
        return self.color

    def get_box(self):
        return self.box
    
    def get_cost(self):
        return self.cost
    
    def get_info(self):
        """Infromation about automobile"""
        return f"Modle: {self.model},\nColor: {self.color},\nBox type: {self.box},\nCost: {self.cost}"
    
    def set_model(self, new_model):
        return self.model == new_model

    def set_color(self, new_color):
        return self.color == new_color

    def set_box(self, new_box):
        return self.box == new_box
    
    def set_cost(self, new_cost):
        return self.cost == new_cost

    def update_km(self, new_km):
        self.new_km += 1

class Car_Dealership():
    """New car dealership!"""

    def __init__(self, name_saloon, adress, cars_for_sale):
        self.name_saloon = name_saloon
        self.adress = adress
        self.cars_for_sale = cars_for_sale
        self. num_of_cars = 0
        self.cars = []

    
    def add_cars(self,cars):
        """Adding new cars to Car Dealership"""
        self.cars.append(Auto_mobile)
        self.num_of_students += 1
