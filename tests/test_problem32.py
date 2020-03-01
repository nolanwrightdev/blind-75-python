import unittest
from problems.problem32 import solution


class Test(unittest.TestCase):
	def test(self):
		self.assertTrue(solution('A man, a plan, a canal: Panama'))
		self.assertFalse(solution('race a car'))
