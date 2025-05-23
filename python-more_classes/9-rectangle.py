#!/usr/bin/python3
"""Définition d'une classe vide Rectangle """


class Rectangle:
    """Représente un rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialise un rectangle avec une largeur et une hauteur."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retourne la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur du rectangle avec vérifications."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcule et retourne l'aire du rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calcule et retourne le perimetre du rectangle"""
        if self.__height == 0 and self.__width:
            return 0
        return (self.__width*2) + (self.__height * 2)

    def __str__(self):
        """Calcule et retourne le perimetre du rectangle"""
        if self.height == 0 or self.width == 0:
            return ""
        else:
            lines = []
            for i in range(self.height):
                lines.append(str(self.print_symbol) * self.width)
            return "\n".join(lines)

    def __repr__(self):
        """Calcule et retourne le perimetre du rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Calcule et retourne le perimetre du rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Calcule et retourne le perimetre du rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)
