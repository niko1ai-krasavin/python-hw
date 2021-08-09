#!/usr/bin/python3

print('Please insert a string: ')
x = input()

input_array = x.split()
output_list = list()
map_of_strings = dict()
max_value = 0

for x in input_array:
    key = x.lower()
    if key not in map_of_strings.keys():
        i = 1
    else:
        i = map_of_strings.get(key) + 1
    map_of_strings.update({key: i})
    max_value = i if i > max_value else max_value

for x in map_of_strings.keys():
    if map_of_strings.get(x) == max_value:
        result_string = str(map_of_strings.get(x)) + " - " + x.lower()
        output_list.append(result_string)

print('Output: ')
print("\n".join(output_list))
