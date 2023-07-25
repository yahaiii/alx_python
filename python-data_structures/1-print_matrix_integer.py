#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    # Loop through each row in the matrix
    for row in matrix:
        # Loop through each element in the row
        for element in row:
            # Print the element with proper formatting, followed by a space
            print("{:d}".format(element), end=" ")
        
        # Move to the next line after printing all elements in the row
        print()
