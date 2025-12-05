# Dictionaries 
# Key-value data structure
# Key need to be unique 
# Value can be duplicated 

student = {
    "name": "Alice",
    "age" : 20,
    "grade" : "A",
    "courses": ["Math","Science","English"]
}

# Accessing and modifying 
print(student["name"])      # "Alice"
print(student.get("age"))   #  20
student["age"] = 21         # Modify value 
student["email"] = "alice@email.com" # Add new key-value 

# # Dictionaries Method:

# keys = student.keys()       # Get all keys 
# values = student.values()   # Get all values
# items = student.items()     # Get key-value pairs

# print(keys)
# print(values)
# print(items)

# # Iterating Dictionaries
# for key in student:
#     print(f"{key}: {student[key]}")

# for key, value in student.items():
#     print(f"{key}:{value}")

# # Nested dictionaries 
# company = {
#     "employees" : {
#         "john" : {"age": 30, "department": "IT"},
#         "jane" : {"age": 25, "department": "HR"}

#     }
# }

# print(company["employees"].items())
# print(company["departments"])


# # Exercises:
# # 1.Create a dictionary called student_records with the following information:
# # "student_001": name is "John", age is 19, major is "Computer Science", grades are [85, 92, 78]
# # "student_002": name is "Sarah", age is 20, major is "Biology", grades are [90, 88, 95]