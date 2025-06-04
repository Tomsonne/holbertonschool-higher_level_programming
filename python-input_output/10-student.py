#!/usr/bin/python3
"""My class module"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }
        return self.__dict__
