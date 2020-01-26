import unittest
from problems.problem07 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertTrue(solution('()'))
		self.assertTrue(solution('()[]{}'))
		self.assertFalse(solution('(]'))
		self.assertFalse(solution('([)]'))
		self.assertTrue(solution('{[]}'))
		self.assertTrue(solution('(([]){})'))
