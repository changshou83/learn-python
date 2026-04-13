# tuple: cannot be changed once created, like a list, but it is immutable.
# Tuples are defined using parentheses () instead of square brackets [].
coordinates = (10.0, 20.0)
print(coordinates, coordinates[0], coordinates[1])

for coordinate in coordinates:
    print(coordinate)
