'''
Blind Curated 75 - Problem 48
=============================

Word Search 2
-------------

Given a grid of characters and a set of words, find all the words from the set
that can be found in the grid.

Words can be constructed from letters in sequentially adjacent cells, where
adjacent cells are ones neighboring either horizontally or vertically. The same
letter may not be used more than once in a word.

Assume all characters are lower case English letters.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/word-search-ii/
'''


from collections import defaultdict


class TrieNode:
	def __init__(self):
		self.children = defaultdict(TrieNode)
		self.word = ''
	def insert(self, word, i=0):
		if i == len(word):
			self.word = word
		else:
			self.children[word[i]].insert(word, i + 1)


def solution(board, words):
	'''
	Preprocess the words by merging them into a trie. At each cell in the grid,
	perform a depth-first search to find any and all words which might start
	there.
	'''
	root = TrieNode()
	for word in words:
		root.insert(word)

	result = []
	def dfs(r, c, node):
		if board[r][c] in node.children:
			char = board[r][c]
			node = node.children[char]
			if node.word:
				result.append(node.word)
				node.word = ''
			board[r][c] = '#'
			if r > 0:
				dfs(r - 1, c, node)
			if c > 0:
				dfs(r, c - 1, node)
			if r + 1 < len(board):
				dfs(r + 1, c, node)
			if c + 1 < len(board[r]):
				dfs(r, c + 1, node)
			board[r][c] = char


	for row in range(len(board)):
		for col in range(len(board[row])):
			dfs(row, col, root)

	return result
