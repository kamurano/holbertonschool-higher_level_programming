#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            if num != len(row):
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format, end="")
        print()
