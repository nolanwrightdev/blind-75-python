import unittest
from problems.problem01 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertListEqual(solution([2, 7, 11, 15], 9), [0, 1])
