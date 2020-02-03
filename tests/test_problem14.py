import unittest
from problems.problem14 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
