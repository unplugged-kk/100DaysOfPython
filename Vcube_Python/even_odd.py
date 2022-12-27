num = int(input("Enter a number:"))

if num >= 0:
    if num % 2 == 0:
        print("The num is positive even")
    else:
        print("The num is postive odd")
else:
    print("The num is negative or zero")
