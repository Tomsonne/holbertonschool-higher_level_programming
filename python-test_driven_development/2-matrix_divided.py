#!/usr/bin/python3
def matrix_divided(matrix, div):
    list_error = "matrix must be a matrix (list of lists) of integers/floats"
    len_error = "Each row of the matrix must have the same size"
    div_int_error = "div must be a number"
    div_zero_error = "division by zero"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(list_error)
    if not isinstance(div, (int, float)):
        raise TypeError(div_int_error)
    if div == 0:
        raise ZeroDivisionError(div_zero_error)

    row_length = len(matrix[0])
    new_matrix = []

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(list_error)
        if len(row) != row_length:
            raise TypeError(len_error)

        new_row = []
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(list_error)
            new_row.append(round(item / div, 2))

        new_matrix.append(new_row)

    return new_matrix
