# for...in loop, used to iterate over a sequence (like a list, tuple, string, etc.) or other iterable objects.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# specifying the index of the item in the loop
for idx, fruit in enumerate(fruits):
    print(idx, fruit)
# specifying a range of numbers to loop over
for i in range(5):  # loop from 0 to 4
    print(i)
for i in range(1, 6):  # loop from 1 to 5
    print(i)
for i in range(0, 10, 2):  # loop from 0 to 9 with a step of 2 (even numbers)
    print(i)

# break statement, used to exit a loop prematurely when a certain condition is met.
for i in range(10):
    if i == 5:
        break  # exit the loop when i is 5
    print(i)

# continue statement, used to skip the current iteration of a loop and move on to the next iteration.
for i in range(10):
    if i % 2 == 0:
        continue  # skip the rest of the loop body for even numbers
    print(i)  # this will only print odd numbers

# for-else statement, the else block will be executed if the loop completes normally (i.e., without encountering a break statement).
for i in range(5):
    print(i)
else:
    print("Loop completed without break.")

# while loop, used to execute a block of code as long as a condition is true.
count = 0
while count < 5:
    print(count)
    count += 1  # increment count to avoid infinite loop
