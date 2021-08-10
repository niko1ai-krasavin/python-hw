#!/usr/bin/python3

def convert(x, count):
    number = int(x)
    if number != 1:
        number = number // 2 if number % 2 == 0 else number * 3 + 1
        count = count + 1
        print(number)
        convert(number, count)
    else:
        print(f'Number of steps: ', count)


print('Please enter a start number:')
step_count = 0
convert(input(), step_count)
