#!/usr/bin/python3
"""Module containing lookup function"""


def lookup(obj):
    """Function to return all available attributes and methods of an object"""
    return list(dir(obj))
