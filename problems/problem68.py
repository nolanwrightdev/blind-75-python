'''
Blind Curated 75 - Problem 68
=============================

Top K Frequent Elements
-----------------------

Given a non-empty array of integers, return the **k** most frequent elements.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/top-k-frequent-elements/
'''


import collections


def solution(nums, k):
	'''
	Find the frequencies of all elements in the given array. Using an array of
	`len(nums) + 1` arrays, add each element to the inner array at the index
	corresponding to its frequency. Return **k** elements from the end of the
	array of arrays.
	'''
	if not nums:
		return []

	freqs = collections.Counter(nums)
	buckets = [[] for _ in range(len(nums) + 1)]

	for num, freq in freqs.items():
		buckets[freq].append(num)

	result = []
	while k:
		if buckets[-1]:
			result.append(buckets[-1].pop())
			k -= 1
		else:
			buckets.pop()

	return result
