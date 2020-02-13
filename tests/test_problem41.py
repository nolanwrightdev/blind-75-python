import unittest
from problems.problem40 import solution


class Test(unittest.TestCase):
	def test(self):
		bits = '00000000000000000000000000001011'
		self.assertEqual(solution(int(bits, 2)), 3)
		bits = '00000000000000000000000010000000'
		self.assertEqual(solution(int(bits, 2)), 1)
		bits = '11111111111111111111111111111101'
		self.assertEqual(solution(int(bits, 2)), 31)
