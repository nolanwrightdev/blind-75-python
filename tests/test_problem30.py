import unittest
from problems.problem30 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution([7, 1, 5, 3, 6, 4]), 5)
		self.assertEqual(solution([7, 6, 4, 3, 1]), 0)
