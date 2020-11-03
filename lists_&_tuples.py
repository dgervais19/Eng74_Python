# Collection in python
# Lists? A set of info saved in an order
# Lists are MUTABLE -
# We can add, remove, change an item in the list
# Indexing starts with 0
# Syntax: ["Yogurt", "apple", "milk"]

# shopping_list = ["apple", "milk", "bread"]
# print(shopping_list)
# print(type(shopping_list))

# Look at indexing in the list items

# print(shopping_list[1])
# print(shopping_list[2])
# print(shopping_list[-1])

# MANAGING LISTS
# add an item to this list

# shopping_list.append('eggs')

# append method adds an item at the end of the list
# print(shopping_list)

# how can we remove an item from our list
# shopping_list.remove('apple')
# print(shopping_list)

# how can we remove the last item from our list that we append earlier
# shopping_list.pop()
# print(shopping_list)

# How can I replace an item in my list
# shopping_lists[1] = "fruits"
# print(shopping_lists)

# can we have mixed data types in a list
# mixed_shopping_list = [1,2,3, "apple", "milk", "bread"]
# print(mixed_shopping_list)

# Task: Create a mixed data type list of 7 items
list = [1, 2, 3, "four", "five", "six", 7]

# Display the type of data
for item in list:
     print(type(item))

# add, delete, replace, pop
# list.append("eight")
# list.remove("four")
# list[2] = 5
# list.pop()

# use indexing to print the list in reverse order
# print(list[::-1])


#### TUPLES!!

# Tupples are IMMUTABLE - CANNOT BE CHANGED
# Use case: NI number, DOB, place of birth

# Syntax: we use () to declare a Tuple

short_list = ("paracetemol", "eggs", "supermalt")
print(type(short_list))
short_list[1] = "fruits" # This code throws an error because tuples do not allow us to change anything
print(short_list)


