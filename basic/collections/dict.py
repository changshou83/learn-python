person = {"name": "Alice", "age": 30, "city": "New York"}
print(person)

# access dictionary values by key
print(person["name"], person["age"], person["city"])
print(person.get("name"), person.get("age"), person.get("city")) # get method returns None if key is not found, instead of raising an error like the square bracket notation
print(person.get("country", "Unknown")) # get method with default value, returns "Unknown" if key is not found
# update dictionary values
person["age"] = 31
print(person)
# add new key-value pair
person["hobbies"] = ["reading", "traveling", "cooking"]
print(person)
# remove key-value pair
del person["city"]
print(person)

# loop through dictionary items
for key, value in person.items():
    print(key, value)
for key in person.keys():
    print(key)
for key in sorted(person.keys()):
    print(key)
for value in person.values():
    print(value)

# dict list
people = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]
print(people)

# nested dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "cooking"],
    "education": {
        "degree": "Bachelor's",
        "major": "Computer Science",
        "university": "XYZ University"
    }
}
print(person)
