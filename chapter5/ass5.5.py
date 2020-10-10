# 5.2 Write a program that repeatedly prompts a user
# for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and
# smallest of the numbers. If the user enters anything
# other than a valid number catch it with a try/except
# and put out an appropriate message and ignore the
# number. Enter 7, 2, bob, 10, and 4 and match the output
# below.

smallest = None
largest = None

while True:
    ui = input("enter number > ")

    if ui == "done":
        break

    try:
        user_input = int(ui)
    except:
        print('Invalid input')
        continue

    if smallest is None:
        smallest = user_input
    elif smallest > user_input:
        smallest = user_input

    if largest is None:
        largest = user_input
    elif largest < user_input:
        largest = user_input

print("Maximum is", largest)
print("Minimum is", smallest)
