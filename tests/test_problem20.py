import unittest
from problems.problem20 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution(2), 2)
		self.assertEqual(solution(3), 3)
