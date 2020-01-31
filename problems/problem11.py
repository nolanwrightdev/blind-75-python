'''
Blind Curated 75 - Problem 11
=============================

Combination Sum
---------------

Given a set of candidate numbers and a target number, find all unique
combinations of candidate numbers which sum to the target.

A candidate number may be be used repeatedly to achieve the target sum.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/combination-sum/
'''


def solution(candidates, target):
	'''
	Construct a list for each candidate number. Each space in the list will
	maintain the combinations which sum to the space's index. At each space, the
	combinations can be derived from two previous spaces. This is a bottom-up,
	dynamic programming solution.
	'''
	previous = [None for _ in range(target + 1)]
	current = []
	for cand in candidates:
		current.append([[]])
		for i in range(1, target + 1):
			current.append(previous[i])
			if i - cand >= 0 and current[i - cand]:
				current[i] = current[i] or []
				for combination in current[i - cand]:
					current[i].append(combination + [cand])
		previous, current = current, []
	return previous[target]
