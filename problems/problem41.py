'''
Blind Curated 75 - Problem 41
=============================

Number of 1 Bits
----------------

Given an unsigned integer, return the number of _1_ bits it has.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/number-of-1-bits/
'''


def solution(n):
	'''
	Check if the least significant bit is set and then shave it off. Repeat until
	the input is zero.
	'''
	count = 0
	while n:
		count += n & 1
		n >>= 1
	return count
