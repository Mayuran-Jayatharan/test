# 3rd day of Python Bootcamp, Input and validation 
name = input("Enter your name: ")
height = float(input("Enter your height (cm): ")) #Convert to float 

#Input validation 
while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0:
            break
        else:
            print("Age must be positive!")
    except ValueError :
        print("Please enter a valid number!")

#Output validation
print(f"Hello, {name}!")
print(f"You are {age} years old and {height} in cm tall.")


# Exercise : Create a simple calculator that takes two numbers and an operation from user. 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /):")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero!"
else:
    result = "Error: Invalid operation!"
print(f"The result is: {result}")

# Exercise : Create a simple quiz program with 3 questions. At the end of the quiz, display the score to the user.
Q1 =input ("What is the capital of Malaysia?")
Q2 =input ("What is the national sport of Malaysia ? ")
Q3 =input ("What is the national dish of Malaysia ?")
score = 0
if Q1 == "kuala lumpur":
    score += 1
if Q2 == "Sepak Takraw":
    score += 1
if Q3 == "nasi lemak":
    score += 1
print (f"Your score is {score} out of 3.")