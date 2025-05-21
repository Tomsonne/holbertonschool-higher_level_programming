#!/usr/bin/python3
"""Définition de la classe Square avec gestion de la position."""


class Square:
    """Classe représentant un carré avec taille et position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise le carré avec une taille et une position optionnelles."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retourne la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la taille du carré après validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retourne la position du carré."""
        return self.__position

    @position.setter
    def position(self, value):
        """Définit la position du carré après validation."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size * self.__size

    def my_print(self):
        """Affiche le carré avec '#' en tenant compte de la position."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
