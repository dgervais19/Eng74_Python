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

# How can we fetch the value called "data types"

print(devops_student_data["completed_lesson_names"][1])