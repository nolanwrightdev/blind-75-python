'''
Blind Curated 75 - Problem 16
=============================

Jump Game
---------

Given an array of non-negative integers, you are initially positioned at the
first index of the array. Each element in the array represents your maximum jump
length at that position. Determine if you are able to reach the last index.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/jump-game/
'''


def solution(nums):
	'''
	Starting from the end of the array, check whether the maximum jumping distance
	from each index includes an index from which the end is reachable.
	'''
	min_reachable = len(nums) - 1
	for i in range(len(nums) - 2, -1, -1):
		if i + nums[i] >= min_reachable:
			min_reachable = i
	return min_reachable == 0
