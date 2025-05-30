#!/usr/bin/env python3
"""BIP BIP"""


class SwimMixin:
    """BIP BIP"""
    def swim(self):
        """BIP BIP"""
        print("The creature swims!")


class FlyMixin:
    """BIP BIP"""
    def fly(self):
        """BIP BIP"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """BIP BIP"""
    def roar(self):
        """BIP BIP"""
        print("The dragon roars!")
