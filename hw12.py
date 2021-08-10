#!/usr/bin/python3

def calculate_fibonacci(number):

    first, second = 1, 1
    fibonacci_number = 0
    for i in range(3, number + 1):
        fibonacci_number = first + second
        first, second = second, fibonacci_number

    return fibonacci_number


print(calculate_fibonacci(5432))
