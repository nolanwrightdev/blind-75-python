import unittest
from problems.problem22 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution('ADOBECODEBANC', 'ABC'), 'BANC')
		self.assertEqual(solution('a', 'a'), 'a')
