#!/usr/bin/python3

# It is used for Problem #40
from functools import reduce

# Problem #6
print('Problem #6:', sum([x for x in range(1, 101)]) ** 2 - sum([x**2 for x in range(1, 101)]))

# Problem #9
# It works too long
print('Problem #9:', [(a * b * c) for a in range(1, 1001) for b in range(1, 1001) for c in range(1, 1001) if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2][0])

# Problem #48
print('Problem #48:', sum(pow(i, i) for i in range(1, 1001)) % 10000000000)

# Problem #40
print('Problem #40:', reduce(lambda x, y: int(x) * int(y), [''.join([str(a) for a in range(1, 200001)])[b - 1] for b in (1, 10, 100, 1000, 10000, 100000, 1000000)]))
