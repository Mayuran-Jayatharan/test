# Loops
# For loop: Known iteration 
# While loop: Unknown iteration 
# Rule of thumb: If you can count it use for loop, If you are waiting for a condition use while loop


# For loop

# for i in range(5):  #0, 1 , 2 , 3 ,4
#     print(i)

# for i in range(1,6): # 1, 2, 3, 4, 5
#     print (i)

# for i in range(0,10,2): # 0, 2, 4, 6, 8
#     print(i)

# #While loop 
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# # Loop control statement
# for i in range(10):
#     if i == 3:
#         continue # Skip this iteration 
#     if i == 7:
#         break    #Exit the loop 
#     print(i) 

# Nested Loop:
for i in range(2):
    for j in range(3):
        print(f"({i},{j})")

# Exercise 1: Create a multiplication table generator. 
num =float(input:"Which number would you like to create a multiplication table generator: ")
for i = range(0,11):
    print(f"{num} X {i}= {num*i})
          
#Continue tomorrow 
    