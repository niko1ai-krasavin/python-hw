#!/usr/bin/python3

total_sum = 0

for number in range(1, 1000000, 2):
    if str(number) == str(number)[::-1]:  # check the base 10 number
        if bin(number)[2:] == bin(number)[2:][::-1]:  # check the base 2 number
            total_sum += number

print(total_sum)
