# Variables and Data Types
age = 25
height = 5.8
name = "John"
is_student = True

# Control Structures
if age >= 18:
    print("You are an adult.")

for i in range(5):
    print("Iteration:", i)

# Functions and Modularization
def add_numbers(a, b):
    return a + b

def greet(name):
    return "Hello, " + name + "!"

# Using the functions
result = add_numbers(10, 5)
print("Result:", result)

message = greet("Alice")
print(message)

# Input and Output Handling
user_input = input("Enter your age: ")
try:
    user_age = int(user_input)
    print("You entered:", user_age)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

# Exception Handling
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print("Error:", e)
