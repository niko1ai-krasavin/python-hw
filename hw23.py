#!/usr/bin/python3

import numpy as np


def n_arr(input_array):
    if not input_array:
        return []
    t = tuple(input_array)
    j = np.prod(input_array)
    start_array = [","] * j
    result_array = np.reshape(start_array, t)
    # or return without the function 'tolist()' for pretty output
    return result_array.tolist()


print('First array:')
print(n_arr([2, 2]))
print('Second array:')
print(n_arr([2, 2, 2]))
print('Third array:')
print(n_arr([]))
print('Fourth array:')
print(n_arr([5]))
