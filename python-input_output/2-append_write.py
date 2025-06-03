#!/usr/bin/python3
"""
Module
"""


def append_write(filename="", text=""):
    """
    Ajoute
    """
    with open(filename, "a") as f:
        return f.write(text)
    