'''
Blind Curated 75 - Problem 42
=============================

House Robber
------------

You are a professional burglar planning to rob houses along a street. Each house
has a certain amount of money stashed. The only constraint stopping you from
robbing all of them is that adjacent houses have security systems installed and
they will automatically contact the police if two adjacent houses are broken
into on the same night.

Given a list of non-negative integers representing the amount of money at each
house, determine the maximum amount of money you can rob in night without
alerting the police.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/house-robber/
'''


def solution(nums):
	'''
	This is a bottom-up dynamic programming solution. For each house, add to its
	amount the greater amount from the two possible points from which it could
	have been reached. After this process, the maximum amount that can be robbed
	will exist in one of the final two houses.
	'''
	if len(nums) <= 2:
		return max(nums) if nums else 0

	nums[2] += nums[0]
	for i in range(3, len(nums)):
		nums[i] += max(nums[i - 2], nums[i - 3])
	return max(nums[-2], nums[-1])
