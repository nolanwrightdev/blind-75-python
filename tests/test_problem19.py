import unittest
from problems.problem19 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution(3, 2), 3)
		self.assertEqual(solution(7, 3), 28)
