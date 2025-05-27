# Type casting

# the conversion of data type in to other data type is called type casting

a = int("5")
b = int("3")
print(a +  b)


# Type casting in print function
c = "5"
d = "3"
print(int(a) +  int(b))


# there are two types of type casting explicit and implicit
# explicit type casting is done by the user by using the constructor function like int(), float(), str() etc.
# implicit type casting is done by the python interpreter automatically when it is required
# Example of implicit type casting
x = 5
y = 2.5
z = x + y  # x is int and y is float, so x is implicitly converted to float
print(z)  # Output: 7.5

# Example of explicit type casting
x = 5
y = 2.5
z = x + int(y)  # y is explicitly converted to int
print(z)  # Output: 7

