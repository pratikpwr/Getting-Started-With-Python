

hours = 0.0
rate_per_hr = 0.0

h = input("Enter Hours: ")
rph = input("Enter rate per hour: ")

try:
    hours = float(h)
    rate_per_hr = float(rph)
except:
    print("Enter valid numeric value.")


def compute_pay(hour, rate_per_hour):
    pay = 0.0
    added_pay = 0.0

    if hour <= 40.0:
        pay = hour * rate_per_hour
    else:
        pay = 40.0 * rate_per_hour
        added_hours = hour - 40.0
        added_pay = added_hours * (rate_per_hour * 1.5)
    return pay + added_pay


print("Pay", compute_pay(hours, rate_per_hr))
