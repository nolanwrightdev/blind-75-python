'''
Blind Curated 75 - Problem 50
=============================

Contains Duplicate
------------------

Given an array of integers, find whether the array contains any duplicates.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/house-robber/
'''


def solution(nums):
	'''
	While iterating over the array, add elements to a set. If an element is
	encountered which exists already in the set, then it is a duplicate.
	'''
	s = set()
	for num in nums:
		if num in s:
			return True
		s.add(num)
	return False
