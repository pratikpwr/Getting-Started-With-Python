# Write a program to prompt the user for hours and rate per hour
# using input to compute gross pay. Pay the hourly rate for the
# hours up to 40 and 1.5 times the hourly rate for all hours
# worked above 40 hours. Use 45 hours and a rate of 10.50 per hour
# to test the program (the pay should be 498.75). You should use
# input to read a string and float() to convert the string to a
# number. Do not worry about error checking the user input -
# assume the user types numbers properly.
pay = 0.0
added_pay = 0.0
hour = 0.0
rate_per_hour = 0.0

h = input("Enter Hours: ")
rph = input("Enter rate per hour: ")

try:
    hour = float(h)
    rate_per_hour = float(rph)
except:
    print("Enter valid numeric value.")

if hour <= 40.0:
    pay = hour * rate_per_hour
else:
    pay = 40.0 * rate_per_hour
    added_hours = hour - 40.0
    added_pay = added_hours * (rate_per_hour * 1.5)

total_pay = pay + added_pay

print(total_pay)
