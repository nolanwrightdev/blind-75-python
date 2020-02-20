'''
Blind Curated 75 - Problem 47
=============================

Add and Search Word - Data structure design
-------------------------------------------

Design a data structure that supports adding and searching for words. The words
consist only of lower case English letters. Search strings consist of the same
letters but may also contain a `.` wildcard character, which can match any other
character.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/add-and-search-word-data-structure-design/
'''


class WordDictionary:
	'''
	Use a prefix trie.
	'''
	def __init__(self):
		self.data = [None] * 26
		self.children = []
		self.is_word = False


	def addWord(self, word):
		node = self
		i = 0

		while i < len(word):
			code = WordDictionary._get_char_code(word[i])
			if not node.data[code]:
				break
			node = node.data[code]
			i += 1

		for char in word[i:]:
			child = WordDictionary()
			node.data[WordDictionary._get_char_code(char)] = child
			node.children.append(child)
			node = child

		node.is_word = True


	def search(self, word):
		node = self

		for i in range(len(word)):
			if word[i] == '.':
				return any(child.search(word[i+1:]) for child in node.children)

			node = node.data[WordDictionary._get_char_code(word[i])]
			if not node:
				return False

		return node.is_word


	def _get_char_code(char):
		return ord(char) - ord('a')
