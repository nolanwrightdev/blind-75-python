import unittest
from problems.problem54 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertListEqual(solution([1, 2, 3, 4]), [24, 12, 8, 6])
