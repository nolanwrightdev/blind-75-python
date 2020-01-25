'''
Blind Curated 75 - Problem 04
=============================

Container With Most Water
-------------------------

See description online.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/container-with-most-water/
'''


def solution(hs):
	'''
	First inspect the leftmost and rightmost edges. Record the area. Next inspect
	the taller of the two previous edges and the edge adjacent to the shorter one.
	Repeat the process until there are no more adjacent edges unchecked.
	'''
	max_area = 0
	left, right = 0, len(hs) - 1
	while left < right:
		max_area = max(max_area, min(hs[left], hs[right]) * (right - left))
		if hs[left] < hs[right]:
			left += 1
		else:
			right -= 1
	return max_area
