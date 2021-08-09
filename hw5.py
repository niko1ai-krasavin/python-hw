#!/usr/bin/python3

print('Please insert numbers: ')
x = input()

result = 0
min_value = 1
strings = x.split()
numbers = [int(x) for x in strings]
original_set = set(numbers)
sorted_set = sorted(original_set)

while min_value > 0:
    if min_value not in sorted_set:
        result = min_value
        break
    else:
        min_value = min_value + 1

if not result:
    print('Output is empty!')
else:
    print('Output: ')
    print(result)
