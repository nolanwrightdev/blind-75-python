import unittest
from problems.problem24 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution('12'), 2)
		self.assertEqual(solution('226'), 3)
		self.assertEqual(solution('0'), 0)
