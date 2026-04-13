'''
function syntax:
def function_name(parameters):
    """docstring"""
    statement(s)

params sequence: position argument, *args, default values, **kwargs
'''

# no parameters
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()

# parameters
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
greet_user('jesse')

# default values
def add_numbers(a = 1, b = 2):
    """Return the sum of a and b."""
    return a + b
# call the function with default values
print(add_numbers())
# call the function with specific values
print(add_numbers(5, 3))
# call the function with keyword arguments
print(add_numbers(b=10, a=4))

# arbitrary number of arguments, use *args for positional arguments and **kwargs for keyword arguments
def make_pizza(*toppings, **kwargs):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    if kwargs:
        print("\nAdditional information:")
        for key, value in kwargs.items():
            print(f"- {key}: {value}")
# call the function with different numbers of arguments
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# use keyword arguments to provide additional information
make_pizza('pepperoni', size='large', crust='thin')

# return multiple values using a tuple
def get_name_and_age(name, age):
    """Return a person's name and age."""
    return name, age
name, age = get_name_and_age('Alice', 30)
print(f"Name: {name}, Age: {age}")

'''
advanced function features:
- higher-order functions: functions that take other functions as arguments or return them as results
- lambda functions: anonymous functions defined with the lambda keyword
- closures: functions that remember the environment in which they were created
- decorators: functions that modify the behavior of other functions
- type annotations: a way to specify the expected types of function parameters and return values
- recursive functions: functions that call themselves in order to solve a problem
- generators: functions that yield a sequence of values instead of returning a single value
'''
# higher-order function example
def apply_function(func, value):
    """Apply a function to a value."""
    return func(value)
# use a lambda function as the argument
result = apply_function(lambda x: x**2, 5)
print(result)  # Output: 25

# type annotations example
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"
print(greet("Alice"))  # Output: "Hello, Alice!"

# closure example
def make_multiplier(multiplier):
    """Return a function that multiplies its input by the given multiplier."""
    def multiplier_function(x):
        return x * multiplier
    return multiplier_function
# create a multiplier function that multiplies by 3
times_three = make_multiplier(3)
print(times_three(10))  # Output: 30

# recursive function example
def factorial(n):
    """Return the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120

# decorator example
def uppercase_decorator(func):
    """A decorator that converts the result of a function to uppercase."""
    @functools.wraps(func)  # preserve the original function's metadata
    def wrapper():
        result = func()
        return result.upper()
    return wrapper
@uppercase_decorator
def greet():
    """Return a greeting message."""
    return "Hello, world!"
print(greet())  # Output: "HELLO, WORLD!"

# generator example
def count_up_to(n):
    """Yield numbers from 1 to n."""
    count = 1
    while count <= n:
        yield count
        count += 1
for number in count_up_to(5):
    print(number)  # Output: 1, 2, 3, 4, 5
