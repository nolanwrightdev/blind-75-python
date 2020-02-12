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

import functools
import operator


def product(nums):
	return functools.reduce(operator.mul, nums, 1)


def solution(nums):
	'''
	Find the intervals delimited by zeroes within the input array as well as the
	negative numbers found in each interval. If the interval contains one negative
	number, consider the products of the subintervals on either side of the one
	negative number. If the interval contains an even number of negative numbers,
	consider the product of the entire interval. If the interval contains an odd
	number of negative numbers greater than one, consider the subinterval
	extending from the beginning of the interval up to but not including the last
	negative number and the subinterval beginning right after the first negative
	number and extending through the end of the interval.
	'''
	intervals = [[0]]
	for i, num in enumerate(nums):
		if num <= 0:
			intervals[-1].append(i)
			if num == 0:
				intervals.append([i + 1])
	intervals[-1].append(len(nums))

	max_product = float('-inf')
	for interval in intervals:
		products = [max_product]
		if len(interval) % 2:
			if len(interval) == 3:
				xs = [
				    nums[interval[0]:interval[1]],
				    nums[interval[1] + 1:interval[-1]],
				]
				products.extend([product(x) for x in xs if x])
			else:
				a = nums[interval[0]:interval[1] + 1]
				b = nums[interval[1] + 1:interval[-2]]
				c = nums[interval[-2]:interval[-1]]
				product_b = product(b)
				products.extend(
				    [product(a) * product_b, product_b * product(c)])
		else:
			x = nums[interval[0]:interval[-1]]
			if x:
				products.append(product(x))
		max_product = max(products)

	if max_product == float('-inf'):
		return 0 if len(intervals) > 1 else nums[0]

	return max_product
