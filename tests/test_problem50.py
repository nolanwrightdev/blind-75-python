import unittest
from problems.problem50 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertTrue(solution([1, 2, 3, 1]))
		self.assertFalse(solution([1, 2, 3, 4]))
		self.assertTrue(solution([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
