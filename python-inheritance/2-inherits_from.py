"""
Module: 2-inherits_from

A function that checks if an object is an instance of a class that inherited
(directly or indirectly) from the specified class.

"""

def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to 
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
    """
    Returns:
            bool: True if the object is an instance of a class that inherited (directly or indirectly)
            from the specified class; otherwise False.
    """
