import unittest
from problems.problem42 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution([1, 2, 3, 1]), 4)
		self.assertEqual(solution([2, 7, 9, 3, 1]), 12)
