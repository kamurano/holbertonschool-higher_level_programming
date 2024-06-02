#!/usr/bin/python3
"""Module containing matrix_mul function"""


def matrix_mul(m_a, m_b):
    """Function for multiplying two matrices"""

    # Checking if m_a and m_b are not lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Checking if from m_a and m_b are not lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Checking if m_a or m_b is empty
    if not any(m_a):
        raise ValueError("m_a can't be empty")
    if not any(m_b):
        raise ValueError("m_b can't be empty")

    # Checking if lists in m_a and m_b contains other than int or float
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    # Checking if m_a or m_b is not rectangle
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Checking if they can not be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Doing multiplication
    rows_a, cols_a = len(m_a), len(m_a[0])
    rows_b, cols_b = len(m_b), len(m_b[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
