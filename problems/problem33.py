'''
Blind Curated 75 - Problem 33
=============================

Longest Consecutive Sequence
----------------------------

Given an unsorted array of integers, find the length of the longest consecutive
sequence of integers.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/longest-consecutive-sequence/
'''


def solution(nums):
	'''
	Construct a set of the given numbers. For each number in the set, find the
	longest consecutive streak in which it is included. Unless the number was
	already encountered in the consecutive streak derived from some other number.
	'''
	max_streak = 0
	nums = set(nums)
	considered = set()
	for num in nums:
		if num in considered:
			continue

		streak = 1
		considered.add(num)
		search = [[num - 1, -1], [num + 1, 1]]
		while search:
			s = search.pop()
			if s[0] in nums:
				streak += 1
				considered.add(s[0])
				s[0] += s[1]
				search.append(s)
		max_streak = max(max_streak, streak)
	return max_streak
