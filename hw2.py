#!/usr/bin/python3

print('Please insert a string: ')
x = input()
array_of_strings = x.split()
out = list(dict.fromkeys(array_of_strings))

if not out:
    print('Output is empty!')
else:
    print('Output: ')
    print(" ".join(out))
