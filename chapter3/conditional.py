percentage = input("Enter your percentage: ")

if int(percentage) < 35:
    print("Fail")
elif int(percentage) < 60:
    print("Average")
elif int(percentage) < 90:
    print("Good")
else:
    print("Very Good!")
