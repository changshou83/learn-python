# create a class
class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__private_attribute = "This is a private attribute"  # private attribute

    # method
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def get_private_attribute(self):
        return self.__private_attribute
    
    # static method: does not access instance or class attributes
    @staticmethod
    def is_adult(age):
        return age >= 18
    
    # class attribute
    species = "Homo sapiens"

    # class method: can access class attributes
    @classmethod
    def from_birth_year(cls, name, birth_year):
        from datetime import datetime
        current_year = datetime.now().year
        age = current_year - birth_year
        return cls(name, age)

# create an instance of the class
person1 = Person("Alice", 30)
# call the method
print(person1.greet())

# extend the class with inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying."

# The behavior of an object is determined by special methods (magic methods).
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # length of the object
    def __len__(self):
        return 2  # length of the point (x, y)

    # string representation of the object
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # official string representation of the object, used for debugging
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
    # equality comparison
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    # operator overloading, example: +
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented
    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    # item access
    def __getitem__(self, key):
        if key == 'x':
            return self.x
        elif key == 'y':
            return self.y
        else:
            raise KeyError(f"Key {key} not found")
    
    # item assignment
    def __setitem__(self, key, value):
        if key == 'x':
            self.x = value
        elif key == 'y':
            self.y = value
        else:
            raise KeyError(f"Key {key} not found")
