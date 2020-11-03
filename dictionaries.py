# What is a dictionary
# Dictionary (arrays) is another way managing data more Dynamically
# Key value pairs to store and manage data
# Syntax : {"name": "James"}
# a = {"key": "value"}
# what type of data can store/manage
# Let's create one

devops_student_data = {
    "key": "value",
    "name": "james",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names":["operators", "data types", "variables"] # In order to put more than one value to the key you have to create a list
}


# print(type(devops_student_data))

# display the data by fetching the key "name"
# print(devops_student_data["completed_lessons"])
# print(devops_student_data["name"])
# print(devops_student_data.keys())
# print(devops_student_data["completed_lesson_names"])

# How can I change the value of specific key
# devops_student_data["completed_lessons"] = 3
# print(devops_student_data)
# print(devops_student_data.items())
# How can we fetch the value called "data types"

# print(devops_student_data["completed_lesson_names"][1])

# Task
# create a New dictionary to store user details
user_details = {
    "key": "value",
    "name": "Dono",
    "DOB": "12/02/1940",
    "course:": "Devops",
    "hobbies": ["basketball", "Piano", "Gym", "Socialising", "data types"]
}
print(user_details)

# Managing the list within the dictionary
user_details["hobbies"].append("running")
user_details["hobbies"].remove("data types")

# all the details that you utilised in the last task
# methods of dictionary to remove, add, replace, display the type of items
user_details["age"] = "40"
print(user_details)

# create a list of hobbies of at least 3 items
# display data in reverse order of hobby list
