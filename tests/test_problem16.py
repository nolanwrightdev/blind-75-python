import unittest
from problems.problem16 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertTrue(solution([2, 3, 1, 1, 4]))
		self.assertFalse(solution([3, 2, 1, 0, 4]))
