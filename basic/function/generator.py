# create generator:
# 1. simple way to create an iterable object;
# 2. use yield keyword to produce a sequence of values;
# 3. lazy evaluation: values are generated on-the-fly as needed, rather than stored in memory all at once;
# 4. efficient for large datasets or infinite sequences
def gen():
    yield 1
    yield 2
    yield 3

# create generator object
g = gen()
# iterate through generator using next() function
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3

# create generator expression:
# 1. concise way to create a generator;
# 2. similar to list comprehensions but with parentheses instead of square brackets;
# 3. generates values on-the-fly as needed, rather than storing them in memory all at once;
# 4. efficient for large datasets or infinite sequences
squares = (x**2 for x in range(5))
# iterate through generator expression using next() function
print(next(squares))  # 0
print(next(squares))  # 1
print(next(squares))  # 4
print(next(squares))  # 9
print(next(squares))  # 16

# send values to generator using send() method, and close generator using close() method
def gen():
    while True:
        value = yield
        print(f"Received: {value}")

g = gen()
next(g)  # Start the generator
g.send("Hello")  # Output: Received: Hello
g.send("World")  # Output: Received: World
g.close()  # Close the generator
