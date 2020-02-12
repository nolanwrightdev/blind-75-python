import unittest
from problems.problem39 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution([3, 4, 5, 1, 2]), 1)
		self.assertEqual(solution([4, 5, 6, 7, 0, 1, 2]), 0)
