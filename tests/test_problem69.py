import unittest
from problems.problem69 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution(1, 2), 3)
		self.assertEqual(solution(-2, 3), 1)
		self.assertEqual(solution(2, 3), 5)
		self.assertEqual(solution(-12, -8), -20)
