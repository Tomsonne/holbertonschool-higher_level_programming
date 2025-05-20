#!/usr/bin/python3
"""Définition d'une classe vide Square (carré)"""


class Square:
    """Classe qui définit un carré avec un attribut privé : la taille"""

    def __init__(self, size=0):
        """Initialisation d'une instance de Square

        Args:
            size: taille du carré (doit être un entier >= 0)

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size  # Attribut privé

    def area(self):
        """Calcule et retourne l'aire du carré"""
        return self.size * self.__size
