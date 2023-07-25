#!/usr/bin/env python3
def no_c(my_string):
    # Initialize an empty string to store the new string without 'c' or 'C'
    new_string = ""
    
    # Iterate through each character in the input string
    for char in my_string:
        # Check if the character is 'c' or 'C'
        if char != 'c' and char != 'C':
            # If it's not 'c' or 'C', append it to the new string
            new_string += char
    
    # Return the new string without 'c' or 'C'
    return new_string
