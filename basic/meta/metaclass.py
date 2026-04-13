# metaclass is a class of a class that defines how a class behaves.
# In Python, everything is an object, including classes themselves.
# By default, the metaclass for all classes is 'type', but you can create your own metaclass by inheriting from 'type' and overriding its methods.
# The most commonly overridden method in a metaclass is __new__, which is called when a new class is created.
# You can use __new__ to modify the class attributes, add new methods, or even change the class name.

# use type to create a class dynamically
def create_class(name):
    return type(name, (object,), {"greet": lambda self: f"Hello from {name}!"})

# Dynamic class creation using a metaclass
class Meta(type):
    # when a new class is created, the __new__ method of the metaclass is called,
    # it receives the name of the class, its base classes, and its attributes as arguments.
    def __new__(cls, name, bases, attrs):
        print(f"Creating class {name} with Meta")
        return super().__new__(cls, name, bases, attrs)
    
    # when the class is initialized, the __init__ method of the metaclass is called,
    # it receives the same arguments as __new__, but it is called after the class is created,
    # it can be used to perform additional initialization tasks, such as registering the class in a registry or adding additional attributes to the class.
    def __init__(cls, name, bases, attrs):
        print(f"Initializing class {name} with Meta")
        super().__init__(name, bases, attrs)

# Dynamically create a class using the Meta metaclass
class MyClass(metaclass=Meta):
    def method(self):
        return "Hello, World!"
