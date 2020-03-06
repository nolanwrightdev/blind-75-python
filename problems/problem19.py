'''
Blind Curated 75 - Problem 19
=============================

Unique Paths
------------

A robot is located at the top-left corner of a _m x n_ grid. The robot can only
move either down or to the right at any point in time. The robot is trying to
reach the bottom-right corner of the grid. How many possible unique paths are
there?

[→ LeetCode][1]

[1]: https://leetcode.com/problems/unique-paths/
'''

def solution(m, n):
	'''
	The number of ways to get to some cell in the grid is equal to the sum of the
	number of ways to get to its neighboring cells. Cells in the same row or
	column as the start position can only be reached one way.
	'''
	grid = [[1] * m for _ in range(n)]

	for row in range(1, n):
		for column in range(1, m):
			grid[row][column] = grid[row-1][column] + grid[row][column-1]

	return grid[n-1][m-1]
