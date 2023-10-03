#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_positive_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_negative_integer(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_single_integer(self):
        self.assertEqual(max_integer([7]), 7)

    def test_duplicate_max_integer(self):
        self.assertEqual(max_integer([1, 2, 2, 1]), 2)


if __name__ == '__main__':
    unittest.main()
