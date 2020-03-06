import unittest
from problems.problem21 import solution


class Test(unittest.TestCase):
	def test(self):
		matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
		solution(matrix)
		self.assertListEqual(matrix, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])
		matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
		solution(matrix)
		self.assertListEqual(matrix,
		                     [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
