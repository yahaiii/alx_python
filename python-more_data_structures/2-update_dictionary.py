#!/usr/bin/env python3
def update_dictionary(a_dictionary, key, value):
    # Create a new dictionary with the same content as a_dictionary
    new_dict = dict(a_dictionary)

    # Update the new dictionary with the new key-value pair
    new_dict[key] = value

    # Return the new dictionary
    return new_dict
