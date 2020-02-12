import unittest
from problems.problem38 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution([2, 3, -2, 4]), 6)
		self.assertEqual(solution([-2, 0, -1]), 0)
		self.assertEqual(solution([0]), 0)
		self.assertEqual(solution([3, -1, 4]), 4)
		self.assertEqual(solution([-2]), -2)
		self.assertEqual(solution([1, 0, -1, 2, 3, -5, -2]), 60)
