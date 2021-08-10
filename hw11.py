#!/usr/bin/python3

def letters_range(start, stop, step=None):
    abc = []
    i = 1 if step is None else int(step)
    for k in range(ord(start), ord(stop), i):
        abc.append(chr(k))
    print(f'Result array:\n', abc)


# ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v']
letters_range('b', 'w', 2)

# ['a', 'b', 'c', 'd', 'e', 'f']
letters_range('a', 'g')

# ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
letters_range('g', 'p')

# ['p', 'n', 'l', 'j', 'h']
letters_range('p', 'g', -2)

# []
letters_range('a', 'a')
