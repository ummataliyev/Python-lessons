class User:
    def __init__(self, name, email):
        self.name = name
        self.email =  email

    
    def login(self):
        print(f"{self.name} login")
    
    
    def logout(self):
        print(f"{self.name} logout")
    

class Student(User):
    def sumbit_task(self):
        print(f"{self.name} task submitted")
    

class Mentor(User):
    def check_task(self):
        print(f"{self.name} task checked")
    

    def login(self):
        print(f"{self.name} login as mentor")



student = Student("Umidjon", "djohnummataliyev@gmail.com")

mentor = Mentor("Muhammadali", "Muhammadali17_abc@gmail.com")

student.login()
student.logout()
student.sumbit_task()
mentor.check_task()
