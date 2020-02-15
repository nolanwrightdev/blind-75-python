import unittest
from problems.problem43 import solution


class Test(unittest.TestCase):
	def test(self):
		grid = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'],
		        ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]
		self.assertEqual(solution(grid), 1)
		grid = [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'],
		        ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
		self.assertEqual(solution(grid), 3)
