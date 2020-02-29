'''
Blind Curated 75 - Problem 72
=============================

Non-overlapping Intervals
-------------------------

Given a collection of intervals, find the minimum number of intervals you need
to remove to make the rest of the intervals non-overlapping.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/non-overlapping-intervals/
'''

def solution(intervals):
	'''
	Sort the intervals by start time. If two intervals are conflicting, remove the
	one which ends earlier.
	'''
	if not intervals:
		return 0

	intervals.sort(key=lambda x: x[0])
	removed_count = 0
	last = intervals[0]
	for curr in intervals[1:]:
		if curr[0] < last[1]:
			removed_count += 1
			last = last if last[1] < curr[1] else curr
		else:
			last = curr
	return removed_count
