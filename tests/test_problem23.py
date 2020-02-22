import unittest
from problems.problem23 import solution


class Test(unittest.TestCase):
	def test(self):
		board = [
		    ['A', 'B', 'C', 'E'],
		    ['S', 'F', 'C', 'S'],
		    ['A', 'D', 'E', 'E'],
		]
		self.assertTrue(solution(board, 'ABCCED'))
		self.assertTrue(solution(board, 'SEE'))
		self.assertFalse(solution(board, 'ABCB'))
