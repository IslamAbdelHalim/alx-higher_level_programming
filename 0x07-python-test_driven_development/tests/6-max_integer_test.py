#!/usr/bin/python3
"""Unittest for max_integer([])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest form max_integer"""
    def test_no_arg(self):
        self.assertEqual(max_integer(), None)

