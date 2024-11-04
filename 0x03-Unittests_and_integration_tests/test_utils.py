#!/usr/bin/env python3

'''
  test_utils.py

  Description:
  Test file that tests the function `utils.access_nested_map`.

  Author: Gadoskey
'''

import unittest
from utils import access_nested_map  # The function to be tested


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function."""

    @parameterized.expand
    def test_access_nested_map(self):
        """Test access_nested_map with a valid path."""
        self.assertEqual(access_nested_map(nested_map={"a": 1}, path=("a",)), 1)
        self.assertEqual(access_nested_map(nested_map={"a": {"b": 2}}, path=("a",)), {'b': 20})
        self.assertEqual(access_nested_map(nested_map={"a": {"b": 2}}, path=("a", "b")), 2)

if __name__ == '__main__':
    unittest.main()
