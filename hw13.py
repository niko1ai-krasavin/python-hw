#!/usr/bin/python3

def do_conversion(temp, scl):
    if scl.lower() == 'f':
        return "%.2f C" % (5/9 * (float(temp) - 32))
    elif scl.lower() == 'c':
        return "%.2f F" % (9/5 * (float(temp)) + 32)
    else:
        return 'Please enter correct data...'


print("Please enter 'F' if you want to convert the temperature from Fahrenheit to Celsius")
print("... or enter 'C' if you want to convert the temperature from Celsius to Fahrenheit:")
scale = input()
print("Enter the temperature value you want to convert in the specified scale:")
temp_value = input()

print(do_conversion(temp_value, scale))
