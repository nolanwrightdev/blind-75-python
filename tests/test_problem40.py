import unittest
from problems.problem40 import solution


class Test(unittest.TestCase):
	def test(self):
		bits_in = '00000010100101000001111010011100'
		bits_out = '00111001011110000010100101000000'
		self.assertEqual(solution(int(bits_in, 2)), int(bits_out, 2))
		bits_in = '11111111111111111111111111111101'
		bits_out = '10111111111111111111111111111111'
		self.assertEqual(solution(int(bits_in, 2)), int(bits_out, 2))
