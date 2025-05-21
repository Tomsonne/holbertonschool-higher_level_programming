#!/usr/bin/python3
"""Définition de la classe Square (carré) avec accès contrôlé à la taille."""


class Square:
    """Classe représentant un carré."""

    def __init__(self, size=0):
        """Initialise un carré avec une taille donnée (par défaut 0).

        Args:
            size (int): La taille du carré, doit être un entier >= 0.
        """
        self.size = size  # Utilise le setter pour la validation

    @property
    def size(self):
        """Accède à la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Modifie la taille du carré avec validation.

        Args:
            value (int): Nouvelle taille du carré.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size * self.__size
