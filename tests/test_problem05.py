import unittest
from problems.problem05 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertCountEqual(solution([-1, 0, 1, 2, -1, -4]),
		                      [[-1, 0, 1], [-1, -1, 2]])
