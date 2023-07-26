#!/usr/bin/env python3
def square_matrix_simple(matrix=[]):
    # Create an empty matrix to store the squared values
    squared_matrix = []

    # Loop through each row in the original matrix
    for row in matrix:
        # Create an empty list to store the squared values of the current row
        squared_row = []

        # Loop through each element in the row and calculate its square
        for element in row:
            squared_value = element ** 2
            squared_row.append(squared_value)

        # Add the squared row to the squared_matrix
        squared_matrix.append(squared_row)

    return squared_matrix
