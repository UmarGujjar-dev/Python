# input function in python

Name = input("Enter your name: ")
print(f"Hello, {Name}! Welcome to the program.")
# This code snippet demonstrates how to use the input function in Python
# to get user input and print a greeting message.

x = input("Enter a number: ")
y = input("Enter another number: ")

# The input function returns a string, so we need to convert it to an integer or float for calculations
print(f"The sum of {x} and {y} is: {int(x) + int(y)}")