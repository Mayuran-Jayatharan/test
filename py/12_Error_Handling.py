# Error Handling: process of anticipating, catching, and managing errors that occur during program execution
# 
# Basic Exception Handling 
# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(f"Result: {result}")
# except ValueError:
#     print("Invalid input! Please enter a number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# Using else and finally
try:
    file = open("data.txt" , "r")
except FileNotFoundError:
    print("File not found!")
else:
    # Executes if no exception occured 
    content = file.read()
    print("File read successfully")
finally:
    # Always executes
    if 'file' in locals() and not file.closed:
        file.close()
    print("Cleanup completed")



