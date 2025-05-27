#!/usr/bin/python3
"""
bip
bip
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initialise un rectangle avec une largeur et une hauteur.

    Les valeurs sont validées à l'aide de integer_validator
    hérité de BaseGeometry.

    Args:
        width (int): La largeur du rectangle.
        height (int): La hauteur du rectangle.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
