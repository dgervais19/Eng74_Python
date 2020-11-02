# What is concatenation?

# first_name = "James"
# middle_name = "Bond"
# last_name = "007"
# age = 18

# print(first_name + " " + middle_name + " " + last_name, str(age))
# print(int(last_name))

# Casting is used to cast int to string or the other way around
# str()


# Get user data
# display message your age is +
# address - including post code and first line of address - house numner
# DOB

# name = input("What is your name? ")

# DOB = input("What is your Date of Birth? (dd/mm/yyyy) ")

# age = int(input("How old are you? "))

# address = input("What is the first line of your address? ")

# post_code = input("Please enter your post code ")

# print("Hello" + " " + name, "You are", str(age), "years old")
# print("You live at", address, ",", post_code)



# Declaring strings with double and single quotes
# "" as well as ''

# single_quotes = 'single quotes\'wow\''
# print(single_quotes)

# double_quotes = "double quotes 'wow' "
# print(double_quotes)


# String slicing - why -
# indexing in python starts from 0
# [start:end]
# greetings = "Hello World!"
# print(greetings[0:5])

# white_spaces = "lots of spaces at the end                    "
# print(len(white_spaces))
# print(white_spaces.strip())
# print(len(white_spaces.strip()))
# stip() deletes all the spaces at the end of string

# count() methods it counts the numbers of times any word is available in the string

example_text = "lots of text with some text"

print(example_text.count("text"))
print(example_text.replace("with" , ",")) # Replace the with and put ','