import unittest
import collections
from problems.problem13 import solution


class Test(unittest.TestCase):
	def test(self):
		arg = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
		out = [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]
		res = solution(arg)
		for anagrams in out:
			count = collections.Counter(anagrams)
			self.assertTrue(any([collections.Counter(r) == count
			                     for r in res]))
