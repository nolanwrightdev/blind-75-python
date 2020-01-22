import unittest
from problems.problem02 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution('abcabcbb'), 3)
		self.assertEqual(solution('bbbbb'), 1)
		self.assertEqual(solution('pwwkew'), 3)
