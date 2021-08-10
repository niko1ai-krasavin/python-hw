#!/usr/bin/python3

import re

print('Please insert the numbers: ')
seq = input()

strings = re.findall(r'[-|+]?\d+', seq)
numbers = [int(x) for x in strings]
result_sum = sum(numbers)

print('Output: ')
print(result_sum)
