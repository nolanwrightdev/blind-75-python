import unittest
from problems.problem59 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution([3, 0, 1]), 2)
		self.assertEqual(solution([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
