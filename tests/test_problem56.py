import unittest
from problems.problem56 import Interval, solution


class Test(unittest.TestCase):
	def test(self):
		self.assertFalse(
		    solution([Interval(0, 30),
		              Interval(5, 10),
		              Interval(15, 20)]))
		self.assertTrue(solution([Interval(5, 8), Interval(9, 15)]))
