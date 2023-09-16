"""
This module tests the floyd_warshall function from floyd_iterative.py
"""

import unittest
from floyd_iterative import floyd_warshall  # Import your function

class TestFloydIterative(unittest.TestCase):
    """
    This class tests the floyd_warshall function
    """

    def setUp(self):
        self.graph = [
            [0, 7, float('inf'), 8],
            [float('inf'), 0, 5, float('inf')],
            [float('inf'), float('inf'), 0, 2],
            [float('inf'), float('inf'), float('inf'), 0]
        ]

    def test_iterative(self):
        """Test the floyd_warshall function."""
        dist_matrix = floyd_warshall(self.graph)  # Your function

        # Add some assertions based on what you expect `dist_matrix` to be
        self.assertEqual(dist_matrix[0][0], 0)
        self.assertEqual(dist_matrix[0][1], 7)
        self.assertEqual(dist_matrix[0][2], 12)
        self.assertEqual(dist_matrix[0][3], 8)

if __name__ == '__main__':
    unittest.main()
