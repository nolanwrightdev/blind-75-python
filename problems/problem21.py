'''
Blind Curated 75 - Problem 21
=============================

Set Matrix Zeroes
-----------------

Given a _m x n_ matrix, if an element is 0, set its entire row and column to 0.
Do it in-place.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/set-matrix-zeroes/
'''

def solution(matrix):
	'''
	Use the first row and column to track whether the whole row or whole column
	should be zeroed out. Of course, before changing the first row or column,
	check if they themselves hold any zeroes. At the end, set to zero all rows
	and columns where the value at the beginning of the row or column is zero.
	'''
	if not matrix:
		return matrix

	rows = len(matrix)
	cols = len(matrix[0])

	zero_first_row = any(matrix[0][c] == 0 for c in range(cols))
	zero_first_col = any(matrix[r][0] == 0 for r in range(rows))

	for r in range(1, rows):
		for c in range(1, cols):
			if matrix[r][c] == 0:
				matrix[0][c] = 0
				matrix[r][0] = 0

	for c in range(1, cols):
		if matrix[0][c] == 0:
			for r in range(1, rows):
				matrix[r][c] = 0

	for r in range(1, rows):
		if matrix[r][0] == 0:
			for c in range(1, cols):
				matrix[r][c] = 0

	if zero_first_row:
		for c in range(cols):
			matrix[0][c] = 0

	if zero_first_col:
		for r in range(rows):
			matrix[r][0] = 0
