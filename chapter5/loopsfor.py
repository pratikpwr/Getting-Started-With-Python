# for loops
largest_number = None
for number in [23, 43, 55, 12, 76, 129, 15, 6]:
    # following if block will run only one time
    if largest_number is None:
        largest_number = number
    if number > largest_number:
        largest_number = number

print(largest_number)
