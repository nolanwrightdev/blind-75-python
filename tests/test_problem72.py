import unittest
from problems.problem72 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)
		self.assertEqual(solution([[1, 2], [1, 2], [1, 2]]), 2)
		self.assertEqual(solution([[1, 2], [2, 3]]), 0)
