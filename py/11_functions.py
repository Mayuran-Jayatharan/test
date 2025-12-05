# Functions 
# # Function: Reusable block of code that do specific task
# def greet_person(name):
#     print(f"Hello, {name}!")

# greet_person("Alice")

# # Functions with return values
# def add_numbers(a, b):
#     return a + b
# result = add_numbers(5, 3)
# print(result)               # 8

# Default parameters 
# def greet_with_title(name,title= "Mr."):
#     return f"Hello, {title} {name}!"

# print(greet_with_title("Smith"))            # "Hello, Mr. Smith!"
# print(greet_with_title("Johnson","Dr."))    # "Hello, Dr. Johnson!"

# #args :
# # - access by index:args[0]
# # unpacking: func(*list)
# def sum_all(*args):
#     return sum(args)
# print(sum_all(1, 2, 3, 4, 5))  #15

# # **kwargs - keyword arguments
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_info(name="Alice", age=25, city="New York")

# # Combining *args and **kwargs
# def flexible_function(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# flexible_function(1, 2, 3, name="Alice", age=25)

# Lambda :
# - anonymous function 
# - small function 

square = lambda x: x**2
print(square(5)) #25

add = lambda x, y: x + y
print(add(3,4))  #7 


