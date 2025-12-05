# Sets 
# A set of data with curly bracket {...}
# Unordered collection of elements

# fruits = {"apple", "banana", "orange"}
# numbers = {1, 2, 3, 4, 5}

# # Set operations 
# fruits.add("grape")         # Add element
# fruits.remove("banana")     # Remove element 
# fruits.discard("kiwi")      # Remove if exists (no error)

# print(fruits)


# Sets mathematic operations:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))         # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2))  # {3,4}
print(set1.difference(set2))    # {1, 2}


# Exercise
grades = [
    ("Alice", "Math", 85),
    ("Bob", "Science", 92),
    ("Alice", "Science", 78),
    ("Charlie", "Math", 90),
    ("Bob", "Math", 88),
    ("Alice", "English", 95)
]

# Find all unique students using sets
students = set()
for grade in grades:
    students.add(grade[0])  # grade[0] is the student name
print("Unique students:", students)

# Find all unique subjects using sets
subjects = set()
for grade in grades:
    subjects.add(grade[1])  # grade[1] is the subject
print("Unique subjects:", subjects) 

# Find all unique grades using sets 
Student_grades = set()
for grade in grades
