#!/usr/bin/python3
"""Function for adding 2 integers"""


def add_integer(a, b=98):
    """Function that adds 2 integers."""
    listo = [int, float]
    if type(a) not in listo:
        raise TypeError("a must be an integer")
    if type(b) not in listo:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
