'''
Blind Curated 75 - Problem 10
=============================

Search in Rotated Sorted Array
------------------------------

Suppose an array sorted in ascending order is rotated at some pivot unknown to
you beforehand.

You are given a target value to search for. If found in the array, return its
index, otherwise -1.

You may assume no duplicate exists in the array.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/search-in-rotated-sorted-array/
'''


def solution(nums, target):
	'''
	Perform a binary search to find the smallest number in the array, and
	consequently the number of rotations. Then perform a second binary search,
	displaced by the number of rotations.
	'''
	if not nums:
		return -1
	l, r = 0, len(nums) - 1
	while l < r:
		m = (l + r) // 2
		if nums[m] < nums[r]:
			r = m
		else:
			l = m + 1
	rotations = l
	l, r = 0, len(nums) - 1
	while l < r:
		m = (l + r) // 2
		m_rot = (m + rotations) % len(nums)
		if target < nums[m_rot]:
			r = m
		elif target > nums[m_rot]:
			l = m + 1
		else:
			return m_rot
	final_guess = (l + rotations) % len(nums)
	return final_guess if nums[final_guess] == target else -1
