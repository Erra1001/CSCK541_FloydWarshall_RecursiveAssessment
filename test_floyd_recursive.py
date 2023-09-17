"""
This module contains unit tests for the floyd_recursive function.
"""

import unittest
from floyd_recursive import floyd_recursive

class TestFloydRecursive(unittest.TestCase):
    """
    TestCase class for floyd_recursive function.
    """
    def setUp(self):
        """
        Set up the test case.
        """
        self.graph = [
            [0, 7, float('inf'), 8],
            [float('inf'), 0, 5, 7],
            [float('inf'), float('inf'), 0, 2],
            [float('inf'), float('inf'), float('inf'), 0]
        ]

    def test_recursive(self):
        """
        Test the floyd_recursive function.
        """
        num_vertices = len(self.graph)
        dist = [[float('inf') for _ in range(num_vertices)] for _ in range(num_vertices)]

        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = floyd_recursive(self.graph, i, j, num_vertices - 1) 

        self.assertEqual(dist[0][0], 0)
        self.assertEqual(dist[0][1], 7)
        self.assertEqual(dist[0][2], 12)
        self.assertEqual(dist[0][3], 8)
        self.assertEqual(dist[1][0], float('inf'))
        self.assertEqual(dist[1][1], 0)
        self.assertEqual(dist[1][2], 5)
        self.assertEqual(dist[1][3], 7)
        self.assertEqual(dist[2][0], float('inf'))
        self.assertEqual(dist[2][1], float('inf'))
        self.assertEqual(dist[2][2], 0)
        self.assertEqual(dist[2][3], 2)
        self.assertEqual(dist[3][0], float('inf'))
        self.assertEqual(dist[3][1], float('inf'))
        self.assertEqual(dist[3][2], float('inf'))
        self.assertEqual(dist[3][3], 0)

if __name__ == "__main__":
    unittest.main()
