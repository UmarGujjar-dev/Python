# Starting if else statements


# drivingage = int(input("What is your age? "))
# print(f"You are {drivingage} years old.")

# if(drivingage>= 18):
#     print("You are old enough to drive.")
# elif(drivingage < 18 and drivingage >= 16):
#     print("You can drive with a learner's permit.")
# elif(drivingage < 0):
#     print("Congratulations on being born!")
# else:
#     print("You are not old enough to drive yet.")



# nested if eles statements
drivingage = int(input("What is your age? "))
if(drivingage >= 18):
    print("You are old enough to drive.")
elif(drivingage >= 16):
    print("You can drive with a learner's permit.")
    if(drivingage >= 17):
        print("You can drive with a full license.")
    else:
        print("You can drive with a restricted license.")
elif(drivingage < 0):
    print("Congratulations on being born!")
else:
    print("You are not old enough to drive yet.")


