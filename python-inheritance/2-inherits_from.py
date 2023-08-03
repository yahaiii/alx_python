"""
Module: 2-inherits_from

This module defines a function that checks if an object is an instance of a class that inherited 
(directly or indirectly) from the specified class.

Functions:
    inherits_from(obj, a_class): Check if the object is an instance of a class that inherited 
    (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if the object is an instance of a class that inherited (directly or indirectly)
        from the specified class; otherwise False.

    Example:
        # >>> class A:
        # ...     pass
        ...
        # >>> class B(A):
        # ...     pass
        ...
        # >>> b = B()
        # >>> inherits_from(b, A)
        True
        # >>> inherits_from(b, B)
        False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
    """
    Returns:
            bool: True if the object is an instance of a class that inherited (directly or indirectly)
            from the specified class; otherwise False.
    """
