#!/usr/bin/python3
"""
Écrit
"""


def write_file(filename="", text=""):
    """
    Lit un fichier
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
