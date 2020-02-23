import unittest
from problems.problem65 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution([1, 2, 5], 11), 3)
		self.assertEqual(solution([2], 3), -1)
