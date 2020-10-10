g = input("Enter your percentage: ")
grade = 0.0

try:
    grade = float(g)
except:
    print("Enter numeric value.")

if 0.0 < grade < 1.0:
    if float(grade) >= 0.9:
        print("A")
    elif float(grade) >= 0.8:
        print("B")
    elif float(grade) >= 0.7:
        print("C")
    elif float(grade) >= 0.6:
        print("D")
    else:
        print("F")
else:
    print("Enter grade between 0.0 and 1.0")
