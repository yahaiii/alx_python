"""This module defines the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """This class represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a rectangle.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            x: The x-coordinate of the rectangle.
            y: The y-coordinate of the rectangle.
            id: The ID of the rectangle.
        """
        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self._width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self._height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self._x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle."""
        self._x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self._y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle."""
        self._y = value


