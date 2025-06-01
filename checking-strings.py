a = "gujjar"

UpperG = a.upper() 
print(a)
print(UpperG)  # Output: None, since print() returns None
print(a)

# precticing traling strings
b = "!!!!!!!Gujjar!!!!!!!!"
print(b)  # Output: !!!!!!!!Gujjar!!!!!!!!
print(b.rstrip('!'))  # Output: Gujjar (removes trailing '!')

print(b.lstrip('!'))  # Output: Gujjar (removes leading '!')

print(b.strip('!'))  # Output: Gujjar (removes leading and trailing '!', ',', and space)

print(b.strip('!').replace('Gujjar', 'Umar Gujjar').upper())  

checking = "gujjarg"
print(checking.islower())
print(checking.isprintable()) 
checking2 = checking.center(30, '-') 
# checking lenth of checking string
print(len(checking2))
print(checking2) 
print(checking.startswith('g'))  # Output: True (checking if the string starts with 'g')
# now checking g is on which index
print(checking2.index('g'))  


# now checking isspace = "   "
isspace_check = "\t"
print(isspace_check.isspace()) 


# Output: True (checking if the string contains only whitespace characters)
# checking if the string is alphanumeric
print(isspace_check.isalnum())  # Output: True (checking if the string is alphanumeric)

# check num 
checknumber = "12345"
print(checknumber.isdigit())  # Output: True (checking if the string contains only digits)

# swapcase_check = "Hello World"
swapcase_check = "Hello World"
print(checknumber.swapcase()) 