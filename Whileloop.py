
# now practicing while loops 

# clientvalue1 = int(input("Enter a starting number: "))
# clientvalue = int(input("Enter an ending number: "))

# while clientvalue1 <= clientvalue:
#     print(clientvalue1)
#     clientvalue1 += 1



# i = int(input("Enter a number to count down from: "))
# while i <= 10:
#     i = int(input("Enter a number to "))
#     print(i)

# print("Countdown complete!")


# decrementing 
# count = 10
# while count >= 0:
#     print(count)
#     count -= 1




# a = ("apple", "banana", "cherry", "date", "elderberry")
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1


# table print 

# a = int(input("Enter a number to print its multiplication table: "))
# i = 1
# while i <= 10:
#     print(f"{a} * {i} = {a * i}")
#     i += 1

# num of list 
# num = [1, 2, 3, 4, 5, 66, 7, 8, 9, 10]

# i = 0
# while i < len(num):
#     print( i , ":", num[i])
#     i += 1


# while i == num[5]:
# #     print("This is the 6th element in the list:", num[i])
#     print("This is the 6th element in the list:", num[i])
#     i += 1


# Pyramid Pattern with Odd Numbers

a = "*"
for i in range(1, 21, 2):  # Start at 1, stop before 21, step by 2 (odd numbers)
    print((a * i).center(20))
for i in range(1, 21, 2):  # Start at 1, stop before 21, step by 2 (odd numbers)
    print((a * i).rjust(20))
for i in range(1, 21, 2):  # Start at 1, stop before 21, step by 2 (odd numbers)
    print((a * i))



# pass statement 
for i in range(5):
    pass

if i> 5:
    pass

print("This is a placeholder for future code.")