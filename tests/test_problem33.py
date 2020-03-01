import unittest
from problems.problem33 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution([100, 4, 200, 1, 3, 2]), 4)
