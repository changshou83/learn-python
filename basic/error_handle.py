# error handle in python
try:
    # code that might raise an exception
    result = 10 / 0
    # raise a custom exception
    raise ValueError("This is a custom error message.")
except ZeroDivisionError as e:
    # handle the specific exception
    print(f"Error: {e}")
except ValueError as e:
    # handle the custom exception
    print(f"Value error: {e}")
except Exception as e:
    # handle any other exception
    print(f"Unexpected error occurred: {e}")
    raise  # re-raise the exception to propagate it further
else:
    # execute this block if no exception occurred
    print(f"Result: {result}")
finally:
    # execute this block regardless of whether an exception occurred
    print("Execution completed.")

'''
Common exceptions in Python include:
- SyntaxError: Raised when there is a syntax error in the code.
- IndexError: Raised when trying to access an index that is out of range.
- KeyError: Raised when trying to access a key that does not exist in a dictionary.
- ValueError: Raised when a function receives an argument of the correct type but an inappropriate value
- TypeError: Raised when an operation is performed on an inappropriate type.
- FileNotFoundError: Raised when trying to open a file that does not exist.
- ZeroDivisionError: Raised when trying to divide by zero.
'''
