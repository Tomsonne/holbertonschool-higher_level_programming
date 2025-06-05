#!/usr/bin/python3
"""
It contains the class:
CustomObject
"""
import pickle


class CustomObject:
    """
    Create class CustomObject
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, Exception):
            return None
