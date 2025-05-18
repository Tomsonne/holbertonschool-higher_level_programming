#!/usr/bin/python3
import unittest
from 6-max_integer import max_integer
class TestMaxInteger(unittest.TestCase):
    
    def test_empty_list(self):
        """Test avec une liste vide"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test avec une liste contenant un seul élément"""
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_elements(self):
        """Test avec une liste de plusieurs éléments"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        """Test avec une liste de nombres négatifs"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        """Test avec une liste de nombres positifs et négatifs mélangés"""
        self.assertEqual(max_integer([1, -2, 3, -4, 5]), 5)

    def test_float_numbers(self):
        """Test avec une liste de nombres à virgule flottante"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 0.5]), 3.5)

    def test_strings(self):
        """Test avec une liste de chaînes de caractères"""
        self.assertEqual(max_integer(['apple', 'banana', 'cherry']), 'cherry')

    def test_identical_elements(self):
        """Test avec une liste où tous les éléments sont identiques"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

if __name__ == '__main__':
    unittest.main()
