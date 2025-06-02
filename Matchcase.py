def check_number(x):
    match x:
        case _ if x < 18 and x > 0:
            print(" not drive")
        case  _ if x >= 18:
            print("drive")
        case _:
            print("just born")

vlay = int(input("Enter a number: "))

check_number(vlay)
# check_number(30)