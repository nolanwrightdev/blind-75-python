'''
Blind Curated 75 - Problem 56
=============================

Meeting Rooms
-------------

Given an array of meeting time intervals consisting of start and end times, find
whether it is possible for one person to attend all meetings.

[→ LintCode][1]

[1]: https://www.lintcode.com/problem/meeting-rooms/description
'''

class Interval():
	def __init__(self, start, end):
		self.start = start
		self.end = end


def solution(intervals):
	'''
	Sort the intervals by start time.
	'''
	intervals.sort(key=lambda x: x.start)
	for a, b in zip(intervals, intervals[1:]):
		if b.start < a.end:
			return False
	return True
