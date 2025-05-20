#!/usr/bin/python3
"""Définition d'une classe vide Square (carré)"""


class Square:
    """Classe qui ne fait rien pour l'instant (classe vide)"""
    def __init__(self, size):
        """Initialisation d'une nouvelle instance de Square

        Args:
            size: La taille du carré (non vérifiée ici)
        """
        self.__size = size  # Attribut privé
