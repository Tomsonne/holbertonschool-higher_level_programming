#!/usr/bin/env python3
"""Notifications"""


class VerboseList(list):
    """Liste"""

    def append(self, item):
        """Ajouter"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Étendre"""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Supprimer"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Extraire"""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
