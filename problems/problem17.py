'''
Blind Curated 75 - Problem 17
=============================

Merge Intervals
---------------

Given a collection of intervals, merge all overlapping intervals

[→ LeetCode][1]

[1]: https://leetcode.com/problems/merge-intervals/
'''


def solution(intervals):
	'''
	Sort the intervals on start time. If an intervals intersects with the last
	merged-in interval, merge it in with that one. Otherwise simply add it to
	the list of merged intervals unchanged.
	'''
	if not intervals:
		return []

	intervals.sort(key=lambda x: x[0])
	result = [intervals[0]]
	for interval in intervals[1:]:
		start, end = interval
		if start <= result[-1][1]:
			result[-1][1] = max(result[-1][1], end)
		else:
			result.append(interval)
	return result
