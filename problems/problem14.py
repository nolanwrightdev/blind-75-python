'''
Blind Curated 75 - Problem 14
=============================

Maximum Subarray
----------------

Given an array of integers, find the contiguous subarray (containing at least
one number) which has the largest sum. Return its sum.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/maximum-subarray/
'''


def solution(nums):
	'''
	Iterate over the array. Add up the numbers so long as the sum remains
	positive. If the sum becomes negative, begin summing from the current number.
	Return the maximum sum found.
	'''
	res = nums[0]
	for i in range(1, len(nums)):
		nums[i] += max(nums[i - 1], 0)
		res = max(res, nums[i])
	return res
