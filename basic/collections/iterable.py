list = [1, 2, 3]
# can be created from any iterable object using the iter() function;
it = iter(list)
# iterate through iterator using next() function
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# raises StopIteration exception when there are no more items to iterate
try:
    print(next(it))  # Raises StopIteration
except StopIteration:
    print("No more items to iterate")

# allows you to traverse through all the elements in a collection, such as a list, tuple, or dictionary;
for item in list:
    print(item)  # 1, 2, 3

# create iterator: an object that implements the iterator protocol, which consists of the __iter__() and __next__() methods;
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
