import unittest
from problems.problem46 import Trie


class Test(unittest.TestCase):
	def test(self):
		trie = Trie()
		trie.insert('apple')
		self.assertTrue(trie.search('apple'))
		self.assertFalse(trie.search('app'))
		self.assertTrue(trie.startsWith('app'))
		trie.insert('app')
		self.assertTrue(trie.search('app'))
