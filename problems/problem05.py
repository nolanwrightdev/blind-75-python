'''
Blind Curated 75 - Problem 05
=============================

3Sum
----

Given an array of integers, find all unique triplets which sum to 0.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/3sum/
'''


def solution(nums):
	'''
	First sort the list. Then for each element in the list, search through the
	rest of the list for possible triplets using the two-pointer method, whereby
	one pointer tracks the element immediately following the first, a second
	pointer tracks the last element, and they gradually move toward each other,
	examining the triplets at each step. How quickly the pointers move depends on
	the elements and their sums.
	'''
	triplets = []
	nums.sort()
	for i, a in enumerate(nums[:-2]):
		if a > 0:
			break
		if i > 0 and a == nums[i - 1]:
			continue
		left, right = i + 1, len(nums) - 1
		while left < right:
			s = a + nums[left] + nums[right]
			if s == 0:
				triplets.append([a, nums[left], nums[right]])
				left += 1
				while left < len(nums) and nums[left - 1] == nums[left]:
					left += 1
				right -= 1
				while right > 0 and nums[right] == nums[right + 1]:
					right -= 1
			elif s > 0:
				right -= 1
				while right > 0 and nums[right] == nums[right + 1]:
					right -= 1
			else:
				left += 1
				while left < len(nums) and nums[left - 1] == nums[left]:
					left += 1
	return triplets
