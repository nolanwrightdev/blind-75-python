import unittest
from problems.problem15 import solution


class Test(unittest.TestCase):
	def test(self):
		res1 = solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
		self.assertListEqual(res1, [1, 2, 3, 6, 9, 8, 7, 4, 5])
		res2 = solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
		self.assertListEqual(res2, [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
		res3 = solution([[1], [2]])
		self.assertListEqual(res3, [1, 2])
