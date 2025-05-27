#!/usr/bin/python3
"""
Module 7-base_geometry
Ce module définit une classe de base pour la géométrie.
"""


class BaseGeometry:
    """Classe de base pour les formes géométriques."""

    def area(self):
        """
        Calcule l'aire de la forme géométrique.
        Doit être surchargée par les classes filles.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que `value` est un entier positif.

        Args:
            name (str): Le nom du paramètre.
            value (int): La valeur à valider.

        Raises:
            TypeError: Si `value` n'est pas un entier.
            ValueError: Si `value` est inférieur ou égal à 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
