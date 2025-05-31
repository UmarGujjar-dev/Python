string = "Gujjar"
dev = string[0:3]  # slicing the first three characters
print(dev)  # Output: Guj
# slicing the last three characters
last_three = string[-3:]  # slicing the last three characters
print(last_three)  # Output: jar
# slicing the middle character(s)
middle = string[3:5]  # slicing the middle characters
print(middle)  # Output: ja 

allstr = len(string)  # length of the string
print(allstr)  # Output: 6
fruit = "banana"
print(fruit[0:len(fruit)-2])  # Output: ban
# slicing the first three characters of 'banana'
print(fruit[:3])  # Output: ban
# slicing the last three characters of 'banana'
print(fruit[-3:])  # Output: ana
# slicing the middle character(s) of 'banana'
print(fruit[3:5])  # Output: na
# slicing the first three characters of 'banana' using negative indexing
print(fruit[-6:-3])  # Output: ban
nm = "Harry"
print(nm[-4:-2]) 