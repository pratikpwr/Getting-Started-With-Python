# The following code will give a throwback
# ValueError: invalid literal for int() with base 10: 'Hello'
# word = "Hello"
# value = int(word)
# print("value: ", value)


# so we use try and except

word = "Hello"
try:
    value = int(word)
except:
    value = int(1)

print("value 1:", value)
