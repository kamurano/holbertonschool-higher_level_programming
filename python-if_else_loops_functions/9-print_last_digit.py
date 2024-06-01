#!/usr/bin/python3
def print_last_digit(number):
    s = str(number)
    s = s[-1]
    k = int(s)
    print(k, end='')
    return k
