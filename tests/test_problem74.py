import unittest
from problems.problem74 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(solution('abc'), 3)
		self.assertEqual(solution('aaa'), 6)
