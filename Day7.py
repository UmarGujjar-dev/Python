# strings
# you can use single or double quotes to create a string
like = 'Python is fun'
# you can use triple quotes to create a multi-line string
like2 = """Python is fun
It is easy to learn"""
print(like + like2)

# search string Index 
print(like[0])  # first character
print(like[-1])  # last character
# slicing string
print(like[0:6])  # first 6 characters
print(like[7:])  # from 7th character to the end
# string length
print(len(like))  # length of the string
# string methods
print(like.lower())  # convert to lower case
print(like.upper())  # convert to upper case
print(like.title())  # convert to title case
print(like.replace('fun', 'awesome').title())  # replace a substring and convert to title case
# string concatenation
print(like + ' and ' + like2)  # concatenate two strings