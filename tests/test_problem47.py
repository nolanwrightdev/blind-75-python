import unittest
from problems.problem47 import WordDictionary


class Test(unittest.TestCase):
	def test(self):
		wd = WordDictionary()
		wd.addWord('bad')
		wd.addWord('dad')
		wd.addWord('mad')
		self.assertFalse(wd.search('pad'))
		self.assertTrue(wd.search('bad'))
		self.assertTrue(wd.search('.ad'))
		self.assertTrue(wd.search('b..'))
