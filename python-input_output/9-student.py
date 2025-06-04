#!/usr/bin/python3
""" My class module
"""


class Student:
    """Defines"""

    def __init__(self, first_name, last_name, age):
        """Initializes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns"""
        return self.__dict__
