import unittest
from problems.problem45 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertTrue(solution(2, [[1, 0]]))
		self.assertFalse(solution(2, [[1, 0], [0, 1]]))
		self.assertTrue(solution(3, [[1, 0], [2, 1]]))
		self.assertFalse(solution(3, [[1, 0], [1, 2], [0, 1]]))
		self.assertTrue(solution(3, [[0, 1], [0, 2], [1, 2]]))
		self.assertFalse(solution(4, [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]))
