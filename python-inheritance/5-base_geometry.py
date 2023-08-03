"""
This module defines the BaseGeometry class.

The BaseGeometry class is an abstract class that cannot be instantiated. It is used as a base class for other classes that will implement the area() method.

The integer_validator() method validates the value. It assumes that the name is always a string. If the value is not an integer, it raises a TypeError exception with the message <name> must be an integer. If the value is less or equal to 0, it raises a ValueError exception with the message <name> must be greater than 0.
"""


class BaseGeometry:
    """
    This class defines two public instance methods:

    * area(): This method raises an exception with the message area() is not implemented.
    * integer_validator(): This method validates the value. It assumes that the name is always a string. If the value is not an integer, it raises a TypeError exception with the message <name> must be an integer. If the value is less or equal to 0, it raises a ValueError exception with the message <name> must be greater than 0.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: The message area() is not implemented
    """

    def __init__(self):
        pass

    def area(self):
        """
        This method raises an exception with the message area() is not implemented.

        The area() method is not implemented because the class BaseGeometry is an abstract class. An abstract class is a class that cannot be instantiated. It is used as a base class for other classes that will implement the abstract methods.

        Args:
            None

        Returns:
            None

        Raises:
            Exception: The message area() is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates the value. It assumes that the name is always a string. If the value is not an integer, it raises a TypeError exception with the message <name> must be an integer. If the value is less or equal to 0, it raises a ValueError exception with the message <name> must be greater than 0.
        Args:
            name (str): The name of the value.
            value (int): The value to be validated.
        Returns:
            None
        Raises:
            TypeError: The message <name> must be an integer
            ValueError: The message <name> must be greater than 0
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

