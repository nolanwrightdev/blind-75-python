import unittest
from problems.problem71 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution('ABAB', 2), 4)
		self.assertEqual(solution('AABABBA', 1), 4)
		self.assertEqual(solution('ABBCCCBBABCDAADCB', 3), 7)
		self.assertEqual(solution('ABBCCCBBABCDAADCB', 4), 9)
		self.assertEqual(solution('ABBBA', 3), 5)
		self.assertEqual(solution('ABBBA', 2), 5)
		self.assertEqual(solution('ABBBA', 1), 4)
		self.assertEqual(solution('AAAA', 2), 4)
		self.assertEqual(solution('JSDSSMESSTR', 2), 6)
