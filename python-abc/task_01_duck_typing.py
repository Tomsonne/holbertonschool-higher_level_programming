#!/usr/bin/env python3
"""
Définition
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Classe abstraite Shape définissant l'interface commune
    pour toutes les formes géométriques.
    """

    @abstractmethod
    def area(self):
        """Méthode abstraite pour calculer l'aire"""
        pass

    @abstractmethod
    def perimeter(self):
        """Méthode abstraite pour calculer le périmètre"""
        pass


class Circle(Shape):
    """Classe représentant un cercle, héritant de Shape"""

    def __init__(self, radius):
        """Initialisation"""
        self.radius = radius

    def area(self):
        """Retourne"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Retourne"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Classe"""

    def __init__(self, width, height):
        """Initialisation"""
        self.width = width
        self.height = height

    def area(self):
        """Retourne"""
        return self.width * self.height

    def perimeter(self):
        """Retourne"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Affiche
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
