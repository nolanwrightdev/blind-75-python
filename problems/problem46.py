'''
Blind Curated 75 - Problem 46
=============================

Implement Trie (Prefix Tree)
----------------------------

Implement a trie with `insert`, `search`, and `startsWith` methods.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/implement-trie-prefix-tree/
'''


class Trie:
	'''
	On the assumption that only lower case characters will be faced, an array of
	size twenty-six is sufficient to capture the characters stored in each node.
	Use recursion to both build up and search through the tree of nodes.
	'''
	def __init__(self):
		self.data = [None] * 26
		self.is_terminal = False


	def insert(self, s):
		if s:
			code = self._get_char_code(s[0])
			if not self.data[code]:
				self.data[code] = Trie()
			self.data[code].insert(s[1:])
		else:
			self.is_terminal = True


	def search(self, s):
		if not s:
			return self.is_terminal
		code = self._get_char_code(s[0])
		if not self.data[code]:
			return False
		return self.data[code].search(s[1:])


	def startsWith(self, s):
		if not s:
			return True
		code = self._get_char_code(s[0])
		if not self.data[code]:
			return False
		return self.data[code].startsWith(s[1:])


	def _get_char_code(self, char):
		return ord(char) - ord('a')
