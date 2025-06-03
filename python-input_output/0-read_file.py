#!/usr/bin/python3
"""Reads"""


def read_file(filename=""):
    """Reads"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
