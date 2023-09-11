"""Unit tests for the floyd_iterative module."""

import unittest
from floyd_iterative import floyd

class TestFloydIterative(unittest.TestCase):
    """Class to test floyd function using iterative method."""

    def test_floyd_iterative_basic(self):
        """Test basic functionality."""
        dist = [
            [0, 1, float('inf'), float('inf')],
            [float('inf'), 0, 2, float('inf')],
            [float('inf'), float('inf'), 0, 3],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        result = floyd(dist)
        self.assertEqual(result[0][1], 1)

    def test_floyd_iterative_advanced(self):
        """Test advanced functionality."""
        dist = [
            [0, 1, float('inf'), float('inf')],
            [float('inf'), 0, 2, float('inf')],
            [float('inf'), float('inf'), 0, 3],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        result = floyd(dist)
        self.assertEqual(result[0][2], 3)

if __name__ == "__main__":
    unittest.main()
