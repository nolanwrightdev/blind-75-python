import unittest
from problems.problem35 import Solution


class Test(unittest.TestCase):
	def test(self):
		solution = Solution()
		self.assertTrue(solution.word_break('leetcode', ['leet', 'code']))
		self.assertTrue(solution.word_break('applepenapple', ['apple', 'pen']))
		self.assertFalse(
		    solution.word_break('catsandog',
		                        ['cats', 'dog', 'sand', 'and', 'cat']))
