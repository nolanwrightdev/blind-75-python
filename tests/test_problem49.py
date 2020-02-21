import unittest
from problems.problem49 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution([2, 3, 2]), 3)
		self.assertEqual(solution([1, 2, 3, 1]), 4)
