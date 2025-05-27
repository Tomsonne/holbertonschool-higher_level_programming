#!/usr/bin/python3
"""
bip
bip
"""


class MyList(list):
    """Classe qui hérite de list avec une méthode"""

    def print_sorted(self):
        """Affiche la liste triée (sans la modifier)."""
        print(sorted(self))
