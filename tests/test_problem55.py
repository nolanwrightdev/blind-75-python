import unittest
from problems.problem55 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertTrue(solution('anagram', 'nagaram'))
		self.assertFalse(solution('rat', 'car'))
