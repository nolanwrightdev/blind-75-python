'''
Blind Curated 75 - Problem 38
=============================

Maximum Product Subarray
------------------------

Given an array of integers, find the maximum product which can be produced from
a contiguous subarray.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/maximum-product-subarray/
'''


def solution(nums):
	'''
	While iterating through the array, maintain a positive product and a negative
	product. The positive product will continue growing by multiplying each number
	it comes across, and vice versa for the negative product. If a negative number
	is encountered, the negative and positive products are swapped until
	potentially another negative number is encountered.
	'''
	res = imax = imin = nums[0]
	for num in nums[1:]:
		if num < 0:
			imax, imin = imin, imax
		imax = max(imax * num, num)
		imin = min(imin * num, num)
		res = max(res, imax)
	return res
