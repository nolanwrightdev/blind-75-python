'''
Blind Curated 75 - Problem 70
=============================

Pacific Atlantic Water Flow
---------------------------

An island is bordered to the West and North by the Pacific Ocean and to the East
and South by the Atlantic Ocean. Given an _m x n_ matrix of non-negative numbers
representing the heights of sections of land on the island, find the sections of
land from which water can flow to both oceans. Water can flow up, down, left, or
right to any section of land of equal or lesser height.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/pacific-atlantic-water-flow/
'''


def solution(matrix):
	'''
	Use two additional matrices to track whether the sections of land can reach
	the oceans. From the respective edges, perform depth-first searches to find
	all the sections of land which can reach each ocean.
	'''
	if not matrix:
		return []

	M = len(matrix)
	N = len(matrix[0])

	can_reach_pacific = [[True] * N] + [[True] + [False] * (N - 1)
	                                    for _ in range(M - 1)]
	stack = [(0, n) for n in range(N)] + [(m, 0) for m in range(1, M)]
	while stack:
		m, n = stack.pop()
		for neighbor in (m + 1, n), (m - 1, n), (m, n + 1), (m, n - 1):
			y, x = neighbor
			if 0 <= y < M and 0 <= x < N and\
                                not can_reach_pacific[y][x] and\
                                matrix[m][n] <= matrix[y][x]:
				can_reach_pacific[y][x] = True
				stack.append(neighbor)

	can_reach_atlantic = [[False] * (N - 1) + [True]
	                      for _ in range(M - 1)] + [[True] * N]
	stack = [(M - 1, n) for n in range(N)] + [(m, N - 1) for m in range(M - 1)]
	while stack:
		m, n = stack.pop()
		for neighbor in (m + 1, n), (m - 1, n), (m, n + 1), (m, n - 1):
			y, x = neighbor
			if 0 <= y < M and 0 <= x < N and\
                       not can_reach_atlantic[y][x] and\
                       matrix[m][n] <= matrix[y][x]:
				can_reach_atlantic[y][x] = True
				stack.append(neighbor)

	result = []
	for m in range(M):
		for n in range(N):
			if can_reach_pacific[m][n] and can_reach_atlantic[m][n]:
				result.append([m, n])

	return result
