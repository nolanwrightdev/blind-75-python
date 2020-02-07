'''
Blind Curated 75 - Problem 15
=============================

Spiral Matrix
-----------------

Given a matrix of _m_ x _n_ elements (_m_ rows, _n_ columns), return all
elements of the matrix in spiral order.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/spiral-matrix/
'''


def solution(matrix):
	'''
	Follow along the edges of the matrix. When reaching a corner, turn clockwise.
	After completing a revolution, take into account that the corners will be
	displaced by one.
	'''
	if not matrix:
		return []

	rows = len(matrix)
	cols = len(matrix[0])
	delta = 0
	result = []
	pos = [0, 0]
	direction = [0, 1]

	while len(result) < rows * cols:
		result.append(matrix[pos[0]][pos[1]])

		if direction[0] > 0:
			if pos[0] == rows - 1 - delta:
				direction = [0, -1]
		elif direction[0] < 0:
			if pos[0] == delta + 1:
				direction = [0, 1]
				delta += 1
		elif direction[1] > 0:
			if pos[1] == cols - 1 - delta:
				direction = [1, 0]
		else:
			if pos[1] == delta:
				direction = [-1, 0]

		pos[0] += direction[0]
		pos[1] += direction[1]

	return result
