import unittest
from problems.problem11 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertCountEqual(solution([2, 3, 6, 7], 7), [[7], [2, 2, 3]])
		self.assertCountEqual(solution([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
