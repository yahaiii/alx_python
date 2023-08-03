"""
This module defines the BaseGeometry class.

The BaseGeometry class is an abstract class that cannot be instantiated. It is used as a base class for other classes that will implement the area() method.

The area() method is not implemented because the class BaseGeometry is an abstract class.
"""


class BaseGeometry:
    """
    This class defines a public instance method called area() that raises an exception with the message area() is not implemented.
    """

    def area(self):
        """
        The area() method is not implemented because the class BaseGeometry is an abstract class. 
        """

        raise Exception("area() is not implemented")
        """
        Raises:
        Exception: The message area() is not implemented
        """

