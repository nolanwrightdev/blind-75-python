import unittest
from problems.problem04 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
		self.assertEqual(solution([2, 3, 4, 5, 18, 17, 6]), 17)
