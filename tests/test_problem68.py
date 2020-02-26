import unittest
from problems.problem68 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertListEqual(solution([1, 1, 1, 2, 2, 3], 2), [1, 2])
		self.assertListEqual(solution([1], 1), [1])
