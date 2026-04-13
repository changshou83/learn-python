# 多态
class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # call the constructor of the parent class
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying."

    # override the greet method
    def greet(self):
        return f"Hello, I am {self.name}, a student with ID {self.student_id}."

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        return f"{self.name} is teaching {self.subject}."

    # override the greet method
    def greet(self):
        return f"Hello, I am {self.name}, a teacher of {self.subject}."
