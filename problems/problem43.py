'''
Blind Curated 75 - Problem 43
=============================

Number of Islands
-----------------

Given a two-dimensional grid of `'1'`s (land) and `'0'`s (water), count the
number of islands. An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically. You may assume all four edges of the
grid are all surrounded by water.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/number-of-islands/
'''

def _get_adjacent(row, col):
	return [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]


def solution(grid):
	'''
	Search through all the cells. If an island is found, visit the rest of the
	cells that make up the island. Use a set to make sure no cell in visited
	twice.
	'''
	if not grid:
		return 0

	R, C = len(grid), len(grid[0])
	visited = set()
	unvisited = [(r, c) for c in range(C) for r in range(R)]

	island_count = 0
	while unvisited:
		cell = unvisited.pop()
		if cell not in visited:
			visited.add(cell)
			r, c = cell
			if grid[r][c] == '1':
				island_count += 1
				adjacent = _get_adjacent(r, c)
				while adjacent:
					cell = adjacent.pop()
					r, c = cell
					if cell not in visited and 0 <= r < R and 0 <= c < C:
						visited.add(cell)
						if grid[r][c] == '1':
							adjacent.extend(_get_adjacent(r, c))

	return island_count
