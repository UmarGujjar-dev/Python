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

checking = "gujjar"
print(checking.islower())