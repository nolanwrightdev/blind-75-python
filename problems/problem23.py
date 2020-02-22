'''
Blind Curated 75 - Problem 23
=============================

Word Search
-----------

Given a two-dimensional board and a word, find whether the word exists in the
board.

Each word must be constructed from letters of sequentially adjacent cells, where
adjacent cells are the ones neighboring either horizontally or vertically. The
same cell may not be used more than once per word.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/word-search/
'''


def solution(board, word):
	'''
	At each cell in the grid, check if the given word starts there. Perform a
	depth-first search to find the whole of the word.
	'''
	if not board:
		return False

	rows = len(board)
	cols = len(board[0])

	def dfs(r, c, i):
		if i == len(word):
			return True
		if 0 <= r < rows and 0 <= c < cols and board[r][c] == word[i]:
			board[r][c] = '#'
			found = any(
			    dfs(a, b, i + 1)
			    for a, b in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)])
			board[r][c] = word[i]
			return found
		return False

	return any(dfs(r, c, 0) for c in range(cols) for r in range(rows))
