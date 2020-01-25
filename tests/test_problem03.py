import unittest
from problems.problem03 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution('babad'), 'bab')
		self.assertEqual(solution('cbbd'), 'bb')
		self.assertEqual(solution('a'), 'a')
		self.assertEqual(solution('bb'), 'bb')
