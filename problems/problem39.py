'''
Blind Curated 75 - Problem 39
=============================

Find Minimum in Rotated Sorted Array
------------

Find the minimum element of an array sorted in ascending order but subsequently
rotated at some unknown pivot.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''


def solution(nums):
	'''
	Perform a simple binary search.
	'''
	left, right = 0, len(nums) - 1
	while left < right:
		mid = (left + right) // 2
		if nums[mid] > nums[right]:
			left = mid + 1
		else:
			right = mid
	return nums[left]
