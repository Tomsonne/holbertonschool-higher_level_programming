#!/usr/bin/env python3
"""Itérateur"""


class CountedIterator:
    """Compteur"""

    def __init__(self, iterable):
        """Initialisation"""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Suivant"""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Compteur"""
        return self.count

    def __iter__(self):
        """Itérable"""
        return self
