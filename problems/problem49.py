'''
Blind Curated 75 - Problem 49
=============================

House Robber 2
--------------

You are a professional burglar planning to rob houses along a street. Each house
has a certain amount of money stashed there. All houses in the neighborhood are
arranged in a circle. That means the first house is the neighbor of the last
one. The only constraint stopping you from robbing all of the houses is that
adjacent houses have security systems installed and they will automatically
contact the police if two adjacent houses are broken into on the same night.

Given a list of non-negative integers representing the amount of money at each
house, determine the maximum amount of money you can rob in one night without
alerting the police.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/house-robber-ii/
'''


def solution(nums):
	'''
	Find the sum of money which can be robbed from all the houses except the last
	one. Find the sum of money which can be robbed from all the houses except the
	first one. Return the greater of the two.
	'''
	if len(nums) <= 3:
		return max(nums) if nums else 0

	max_plan = 0
	for a, b in [(0, -1), (1, len(nums))]:
		plan = [0, 0]
		houses = nums[a:b]
		for house in houses:
			plan.append(max(plan[-1], house + plan[-2]))
		max_plan = max(max_plan, plan[-1])
	return max_plan
