#!/usr/bin/env python3
def update_dictionary(a_dictionary, key, value):
    # Create a new dictionary with the same content as a_dictionary
    new_dict = dict(a_dictionary)

    # Check if the key exists in the original dictionary
    if key in a_dictionary:
        # Update the value associated with the existing key
        new_dict[key] = value
    else:
        # Add the new key-value pair to the new dictionary
        new_dict[key] = value

    # Return the new dictionary
    return new_dict
