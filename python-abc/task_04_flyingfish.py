#!/usr/bin/env python3
"""PoissonVolant"""


class Fish:
    """Poisson"""

    def swim(self):
        """Nager"""
        print("The fish is swimming")

    def habitat(self):
        """Habitat"""
        print("The fish lives in water")


class Bird:
    """Oiseau"""

    def fly(self):
        """Voler"""
        print("The bird is flying")

    def habitat(self):
        """Habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """PoissonVolant"""

    def fly(self):
        """Voler"""
        print("The flying fish is soaring!")

    def swim(self):
        """Nager"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Habitat"""
        print("The flying fish lives both in water and the sky!")
