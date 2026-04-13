# create sets
empty_set = set()
print(empty_set)
from_list = set([1, 2, 3, 4, 5])
print(from_list)
from_string = set("hello")
print(from_string)
from_tuple = set((1, 2, 3, 4, 5))
print(from_tuple)
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)

# access set items, sets are unordered, so you cannot access items by index, but you can check if an item is in the set
print(3 in unique_numbers)  # check if 3 is in the set, returns True
print(6 in unique_numbers)  # check if 6 is in the set, returns False
# add items to set
unique_numbers.add(6)
print(unique_numbers)
unique_numbers.update([7, 8, 9])  # add multiple items to set
print(unique_numbers)
# remove items from set
unique_numbers.remove(9)  # remove item, raises KeyError if item is not found
print(unique_numbers)
unique_numbers.discard(8)  # remove item, does not raise error if item is not found
print(unique_numbers)
unique_numbers.pop()  # remove and return an arbitrary item from the set, raises KeyError if the set is empty
print(unique_numbers)
unique_numbers.clear()  # remove all items from the set
print(unique_numbers)

# loop through set items
for number in from_list:
    print(number)
for number in sorted(from_list):  # sort the set before looping, since sets are unordered
    print(number)
for idx, number in enumerate(from_list): # enumerate the set before looping, since sets are unordered, the index will not correspond to the original order of the items in the set
    print(idx, number)

# set operations
set_c = {1, 2, 3}
set_d = {3, 4, 5}
union = set_c.union(set_d)  # all unique items from both sets, use the | operator as a shorthand for union: set_c | set_d
print(union)
intersection = set_c.intersection(set_d)  # items that are in both sets, use the & operator as a shorthand for intersection: set_c & set_d
print(intersection)
difference = set_c.difference(set_d)  # items that are in set_c but not in set_d, use the - operator as a shorthand for difference: set_c - set_d
print(difference)
symmetric_difference = set_c.symmetric_difference(set_d)  # items that are in either set_c or set_d but not in both, use the ^ operator as a shorthand for symmetric difference: set_c ^ set_d
print(symmetric_difference)
is_subset = set_c.issubset(set_d)  # check if set_c is a subset of set_d, returns False
print(is_subset)
is_superset = set_c.issuperset(set_d)  # check if set_c is a superset of set_d, returns False
print(is_superset)
no_common_items = set_c.isdisjoint(set_d)  # check if set_c and set_d have no common items, returns False
print(no_common_items)
