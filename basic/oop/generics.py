# generics: Generics allow you to create classes and functions that can work with any type of data, while still maintaining type safety.
# This is achieved through the use of type variables, which are placeholders for the actual types that will be used when the class or function
from typing import TypeVar, Generic

# define a type variable
T = TypeVar('T')

# generic class that can hold any type of value
class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get(self):
        return self.value

# generic function that can accept any type of value
def identity(value: T) -> T:
    return value
