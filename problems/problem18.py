'''
Blind Curated 75 - Problem 18
=============================

Insert Interval
---------------

Given a collection of non-overlapping intervals and a new interval to add to the
collection, insert (and merge if necessary) the new interval into the
collection. Assume the collection of intervals is initially sorted by start
time.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/insert-interval/
'''


def solution(intervals, new_interval):
	'''
	This problem can be solved in a few easy steps. Add all the intervals which do
	not intersect with the new interval to another list. Then fully merge the new
	interval with the intervals which intersect it. Add the merged interval to the
	list. Then add the rest of the intervals which also do not intersect with the
	merged interval to the list. Return the list.
	'''
	L, R = len(intervals), []

	i = 0
	while i < L and intervals[i][1] < new_interval[0]:
		R.append(intervals[i])
		i += 1

	if i < L:
		new_interval[0] = min(new_interval[0], intervals[i][0])

	while i < L and intervals[i][0] <= new_interval[1]:
		new_interval[1] = max(new_interval[1], intervals[i][1])
		i += 1

	R.append(new_interval)
	R.extend(intervals[i:])
	return R
