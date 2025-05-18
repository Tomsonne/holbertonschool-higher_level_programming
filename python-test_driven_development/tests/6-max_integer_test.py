#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):  
    def test_max_integer(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([-3]), -3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([15, 10, 5]), 15)
        self.assertEqual(max_integer([15, 10, 5, -5, -10, 15]), 15)
        self.assertEqual(max_integer([15, 15, 15]), 15)

    def test_type_error(self):
        self.assertRaises(TypeError, max_integer, ["h", 1])  
        self.assertRaises(TypeError, max_integer, [2, [2, 1]])

    def test_float_values(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)
        self.assertEqual(max_integer([3.3, 2.2, 1.1]), 3.3)
        self.assertEqual(max_integer([3.0, 3.1, 3.2]), 3.2)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_value(self):
        self.assertEqual(max_integer([100]), 100)

    def test_multiple_values(self):
        self.assertEqual(max_integer([5, 8, 3, 9, 2]), 9)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_non_integer_values(self):
        self.assertRaises(TypeError, max_integer, [2, "hello", 3.5])

    def test_mixed_data_types(self):
        self.assertRaises(TypeError, max_integer, [5, 'string', 10])

