import unittest
from problems.problem10 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution([4, 5, 6, 7, 0, 1, 2], 0), 4)
		self.assertEqual(solution([4, 5, 6, 7, 0, 1, 2], 3), -1)
		self.assertEqual(solution([3, 1], 1), 1)
		self.assertEqual(solution([3, 1], 3), 0)
		self.assertEqual(solution([1, 3, 5], 3), 1)
		self.assertEqual(solution([3, 5, 1], 5), 1)
