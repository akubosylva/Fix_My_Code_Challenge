#!/usr/bin/python3

"""
Module square
describe the class square
"""

class Square():
    """
    Square class represents a square shape with a given width and height.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Square object.

        Args:
            *args: Variable-length arguments.
            **kwargs: Keyword arguments to set object attributes.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """
        Calculate the area of the square.

        Returns:
            The area of the square (width * height).
        """
        return self.width * self.height

    def permiter_of_my_square(self):
        """
        Calculate the perimeter of the square.

        Returns:
            The perimeter of the square (2 * width + 2 * height).
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        String representation of the Square object.

        Returns:
            A string representation of the Square in the format "width/height".
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    
    # Create a Square object with width=12 and height=9
    s = Square(width=12, height=9)

    # Print the string representation of the Square
    print(s)

    # Calculate and print the area of the Square
    print(s.area_of_my_square())

    # Calculate and print the perimeter of the Square
    print(s.permiter_of_my_square())
