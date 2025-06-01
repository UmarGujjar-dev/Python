
time = int(input("Enter the current hour (0-23): "))
# Good morning message based on the time of day


if 5 <= time < 12:
    print("Good morning!")
elif 12 <= time < 18:
    print("Good afternoon!")
elif 18 <= time < 22:
    print("Good evening!")
else:
    print("Good night!")

