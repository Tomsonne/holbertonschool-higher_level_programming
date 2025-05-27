#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of,
or inherits from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """Affiche la liste triée (sans la modifier)."""
    return isinstance(obj, a_class)
