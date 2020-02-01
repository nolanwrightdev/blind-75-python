'''
Blind Curated 75 - Problem 12
=============================

Rotate Image
------------

Rotate an n x n two-dimensional matrix in-place.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/rotate-image/
'''


def solution(matrix):
	'''
	Process the matrix in squares, where each square consists of four spaces on
	the same rotational axis. Repeatedly move the value from the previous space
	into the next, temporarily storing the replaced value.
	'''
	n = len(matrix)
	for i in range(n // 2):
		for j in range(i, n - 1 - i):
			pos = [n - j - 1, i]
			val = matrix[pos[0]][pos[1]]
			for _ in range(4):
				pos[0], pos[1] = pos[1], n - pos[0] - 1
				matrix[pos[0]][pos[1]], val = val, matrix[pos[0]][pos[1]]
