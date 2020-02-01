import unittest
from problems.problem12 import solution


class Test(unittest.TestCase):
	def test(self):
		matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
		solution(matrix)
		self.assertListEqual(matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
		matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7],
		          [15, 14, 12, 16]]
		solution(matrix)
		self.assertListEqual(
		    matrix,
		    [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])
