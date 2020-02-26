import unittest
from problems.problem64 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution([10, 9, 2, 5, 3, 7, 101, 18]), 4)
