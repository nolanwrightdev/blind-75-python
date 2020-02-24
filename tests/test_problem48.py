import unittest
from problems.problem48 import solution


class Test(unittest.TestCase):
	def test(self):
		board = [
		    ['o', 'a', 'a', 'n'],
		    ['e', 't', 'a', 'e'],
		    ['i', 'h', 'k', 'r'],
		    ['i', 'f', 'l', 'v'],
		]
		words = ['oath', 'pea', 'eat', 'rain']
		self.assertCountEqual(solution(board, words), ['eat', 'oath'])
