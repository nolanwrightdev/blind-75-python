'''
Blind Curated 75 - Problem 35
=============================

Word Break
----------

Given a non-empty string and a list of non-empty words, find whether the string
can be segmented into a sequence of one or more words.

Note that the same word may be used multiple times. Assume there are no
duplicate words.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/word-break/
'''

import collections


class TrieNode:
	def __init__(self):
		self.children = collections.defaultdict(TrieNode)
		self.word = ''

	def insert(self, word):
		node = self
		for char in word:
			node = node.children[char]
		node.word = word


class Solution:
	'''
	Preprocess the words into a prefix trie. Use the prefix trie to find all words
	that are prefixes of the given string. Recurse with the suffix of each such
	prefix found. If some combination of prefixes amounts to the entirety of the
	given string, return `True`.
	'''
	def word_break(self, s, words):
		self._s = s
		self._reached = [False] * len(s)
		self._root = TrieNode()
		for word in words:
			self._root.insert(word)
		return self._search_from(0)

	def _search_from(self, i):
		if i == len(self._s):
			return True
		if self._reached[i]:
			return False
		node = self._root
		for j, char in enumerate(self._s[i:], i):
			if char in node.children:
				node = node.children[char]
				if node.word:
					self._reached[j] = True
					if self._search_from(j + 1):
						return True
			else:
				return False
