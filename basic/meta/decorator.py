import time
from functools import wraps

# a decorator is a higher-order function that takes a function as an argument and returns a new function that extends the behavior of the original function.
# for example, logging, timing, access control, or caching.

# receive a function as an argument
def timer(func):
    # receive any number of arguments and keyword arguments, and pass them to the original function.
    # use wraps to preserve the original function's metadata, such as its name(__name__) and docstring(__doc__).
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Execution time: {time.time() - start:4.4f} seconds")
        return result
    return wrapper

# logger decorator can be used to log the function name and its return value, it can be useful for debugging and monitoring the performance of the function.
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

# apply the decorators to the function, the order of the decorators matters, the decorator closest to the function is applied first.
@logger
@timer
def example_function():
    total = 0
    for i in range(1000000):
        total += i
    print(f"Total: {total}")

example_function()
