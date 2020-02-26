'''
Blind Curated 75 - Problem 64
=============================

Longest Increasing Subsequence
------------------------------

Given an unsorted array of integers, find the length of the longest increasing
subsequence.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/longest-increasing-subsequence/
'''


def solution(nums):
	'''
	Find the length of the longest increasing subsequence from index _0_ to index
	_i_ for _i_ in range _[1, n)_. Return the maximum of all such lengths.
	'''
	if not nums:
		return 0

	lengths = [1] * len(nums)

	for i in range(1, len(nums)):
		length = 0
		for j in reversed(range(i)):
			if nums[i] > nums[j]:
				length = max(length, lengths[j])
		lengths[i] = length + 1

	return max(lengths)
