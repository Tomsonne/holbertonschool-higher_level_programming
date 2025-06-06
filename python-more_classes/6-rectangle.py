#!/usr/bin/python3
"""Définition d'une classe vide Rectangle """


class Rectangle:
    """Représente un rectangle."""

    number_of_instances = 0

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
                lines.append("#" * self.width)
            return "\n".join(lines)

    def __repr__(self):
        """Calcule et retourne le perimetre du rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Calcule et retourne le perimetre du rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
