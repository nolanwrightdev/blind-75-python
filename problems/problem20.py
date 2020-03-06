'''
Blind Curated 75 - Problem 20
=============================

Climbing Stairs
---------------

You are climbing a stair case. It takes _n_ steps to reach the top. You can take
either one or two steps at a time. In how many distinct ways can you climb to
the top.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/climbing-stairs/
'''


def solution(n):
	'''
	The number of distinct ways to reach a step is the sum of distinct ways to
	reach the steps from which that step is reachable.
	'''
	a, b = 1, 1
	for _ in range(n-1):
		a, b = b, a+b
	return b
