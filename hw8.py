#!/usr/bin/python3

def convert(x):
    if x.lower() != 'cancel':
        try:
            number = int(x)
            result = number // 2 if number % 2 == 0 else number * 3 + 1
            print(result)
            convert(input())
        except ValueError:
            print('Failed to convert the entered text to a number.')
            convert(input())
    else:
        print('Bye!')


if __name__ == '__main__':
    print('Hello dear user! Please insert a text below:')
convert(input())
