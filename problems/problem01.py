'''
Blind Curated 75 - Problem 01
=============================

Two Sum
-------

Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/two-sum/
'''


def solution(nums, target):
	'''
	While iterating through the input array, store in a hash map the difference
	between the target and the current element as the key and the index of the
	current element as the value. On finding an element whose value exists in the
	hash map, return both its index and the corresponding index in the hash map.
	'''
	targets = {}
	for index, num in enumerate(nums):
		if num in targets:
			return [targets[num], index]
		targets[target - num] = index
