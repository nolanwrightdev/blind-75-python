'''
Blind Curated 75 - Problem 54
=============================

Product of Array Except Self
----------------------------

Given an array of integers, return an array such that each element of the array
amounts to the product of all the elements other than the element at the same
position in the input array.

Solve it without using division.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/product-of-array-except-self/
'''

def solution(nums):
	'''
	Find the cumulative products going from left to right. Find the cumulative
	products going from right to left. To find the total product excluding some
	particular number, multiply the cumulative products reached from either side
	of that number.
	'''
	left_to_right = [1]
	for num in nums:
		left_to_right.append(left_to_right[-1] * num)

	right_to_left = [1]
	for num in nums[::-1]:
		right_to_left.append(right_to_left[-1] * num)

	output = []
	for i in range(len(nums)):
		output.append(left_to_right[i] * right_to_left[len(nums) - 1 - i])
	return output
