# reflect can dynamically get information about object, call methods, and even modify objects at runtime.
# core functions: getattr(obj, name), hasattr(obj, name), setattr(obj, name, value), delattr(obj, name)
# Example usage of reflection in Python: plugin system, common util classes, configuration management.

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# Create an instance of the Calculator class
calc = Calculator()

# dynamically call methods based on user input
method_name = input("Enter the method to call (add/subtract): ")
if hasattr(calc, method_name):
    method = getattr(calc, method_name)
    print(method(10, 5))
else:
    print("Method not found.")
