import unittest
from problems.problem17 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertListEqual(solution([[1, 3], [2, 6], [8, 10], [15, 18]]),
		                     [[1, 6], [8, 10], [15, 18]])
		self.assertListEqual(solution([[1, 4], [4, 5]]), [[1, 5]])
