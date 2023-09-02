"""Unit tests for the floyd_recursive module."""

import unittest
from floyd_recursive import floyd_recursive

class TestFloydRecursive(unittest.TestCase):
    """Class to test floyd_recursive function"""

    def test_floyd_recursive_basic(self):
        """Test basic functionality of floyd_recursive function."""
        dist = [
            [0, 1, float('inf'), float('inf')],
            [float('inf'), 0, 2, float('inf')],
            [float('inf'), float('inf'), 0, 3],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        memo_cache = {}
        result = floyd_recursive(dist, 0, 1, 3, memo_cache)
        self.assertEqual(result, 1)

    def test_floyd_recursive_advanced(self):
        """Test advanced functionality of floyd_recursive function."""
        dist = [
            [0, 1, float('inf'), float('inf')],
            [float('inf'), 0, 2, float('inf')],
            [float('inf'), float('inf'), 0, 3],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        memo_cache = {}
        result = floyd_recursive(dist, 0, 2, 3, memo_cache)
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()
