#!/usr/bin/env python3
def multiple_returns(sentence):
    # Check if the sentence is empty
    if not sentence:
        return (0, None)  # Return a tuple with length 0 and first character as None
    
    # Get the length of the sentence
    length = len(sentence)
    
    # Get the first character of the sentence
    first_character = sentence[0]
    
    # Return the tuple with length and first character
    return (length, first_character)
