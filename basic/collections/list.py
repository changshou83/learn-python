fruits = ["apple", "banana", "cherry"]

# access list items by index
print(fruits, fruits[0], fruits[1], fruits[2])
# if idx is negative, it will count from the end of the list, so -1 is the last item, -2 is the second to last item, and so on
print(fruits[-1], fruits[-2], fruits[-3])

# list length
fruits_length = len(fruits)
print(fruits_length)

# update list
replace_fruit_idx = fruits.index("banana") # find the index of "banana"
fruits[replace_fruit_idx] = "orange"
print(fruits)

# add new fruit
fruits.append("grape")  # add to end of list
print(fruits)
fruits.insert(1, "kiwi")  # insert at index 1, if index is not provided, it will add to end of list
print(fruits)

# remove fruit
fruits.remove("apple")  # remove by value
print(fruits)
fruits.pop(0)  # remove by index, if index is not provided, it will remove the last item
print(fruits)

# sort list
fruits.sort()  # sort the list in place in ascending order
print(fruits)
sorted_fruits = sorted(fruits)  # create a new list that is sorted in ascending order
print(sorted_fruits)
# if you want to sort by some custom criteria, you can provide a function as the key argument to the sort method. For example, to sort by the length of the fruit names:
fruits.sort(key=lambda x: len(x), reverse=False)  # sort by length of fruit names in ascending order
print(fruits)

# reverse list
fruits.reverse()  # reverse the list in place
print(fruits)
reverse_fruits = fruits[::-1]  # create a new list that is the reverse of the original list
print(reverse_fruits)

# for loop
for fruit in fruits:
    print(fruit)
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

# list comprehension, not recommended for complex operations, but can be useful for simple operations
new_fruits = [fruit.upper() for fruit in fruits]  # create a new list with the fruit names in uppercase
print(new_fruits)
filtered_fruits = [fruit for fruit in fruits if "a" in fruit]  # create a new list with only the fruit names that contain the letter "a"
print(filtered_fruits)
all_fruits_have_a = all("a" in fruit for fruit in fruits)  # check if all fruit names contain the letter "a"
print(all_fruits_have_a)
any_fruit_has_a = any("a" in fruit for fruit in fruits)  # check if any fruit name contains the letter "a"
print(any_fruit_has_a)

# create number list
numbers = list(range(1, 11))  # create a list of numbers from 1 to 10, params are start, stop, step
print(numbers)
even_numbers = list(range(2, 11, 2))  # create a new list with only the even numbers
print(even_numbers)
squared_numbers = [num ** 2 for num in numbers]  # create a new list with the squares of the numbers
print(squared_numbers)
max_value = max(numbers)  # find the maximum value in the list
min_value = min(numbers)  # find the minimum value in the list
sum_of_numbers = sum(numbers)  # find the sum of the numbers in the list
print(max_value, min_value, sum_of_numbers)

# slice：syntax is list[start:stop:step], if start is not provided, it will start from the beginning of the list, if stop is not provided, it will go to the end of the list, if step is not provided, it will default to 1
sliced_fruits = fruits[1:4]  # create a new list with the items from index 1 to 3 (4 is not included)
print(sliced_fruits)
sliced_fruits_from_start = fruits[:3]  # create a new list with the first 3 items
print(sliced_fruits_from_start)
sliced_fruits_to_end = fruits[3:]  # create a new list with the items from index 3 to the end of the list
print(sliced_fruits_to_end)
sliced_fruits_with_step = fruits[::2]  # create a new list with every other item in the list
print(sliced_fruits_with_step)
