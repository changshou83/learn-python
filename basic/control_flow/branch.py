age = 18

# simple if statement, need colon and indentation
if age >= 18:
    print("You are an adult.")

# if-else statement
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# if-elif-else statement
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

# match-case statement (Python 3.10+), similar to switch-case in other languages
match age:
    case 0:
        print("You are a newborn.")
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
        print("You are a child.")
    case 13 | 14 | 15 | 16 | 17:
        print("You are a teenager.")
    case _ if age >= 18 and age < 65: # guard condition to match a range of values
        print("You are an adult.")
    case _ if age >= 65:
        print("You are a senior.")
    case _: # default case, matches anything not matched by previous cases
        print("Invalid age.")

# ternary operator (conditional expression)
status = "adult" if age >= 18 else "minor"
print(f"You are an {status}.")

# multiple conditions with logical operators
if age >= 18 and age < 65:
    print("You are an adult.")
elif age >= 65 or age < 18:
    print("You are a senior.")
elif age < 18 or not age >= 18:
    print("You are a minor.")

# membership check
name = "Alice"
admin_list = ["Alice", "Bob", "Charlie"]
if name in admin_list:
    print(f"{name} is an admin.")
elif name not in admin_list:
    print(f"{name} is not an admin.")

if admin_list:
    print("Admin list is not empty.")

# equality check
# double equals for comparison, single equals is assignment
if name == "Alice":
    print("Hello, Alice!")
elif name != "Bob":
    print("You are not Bob.")
