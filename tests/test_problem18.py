import unittest
from problems.problem18 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
		self.assertEqual(
		    solution([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
		    [[1, 2], [3, 10], [12, 16]])
