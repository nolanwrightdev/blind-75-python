'''
Blind Curated 75 - Problem 40
=============================

Reverse Bits
------------

Reverse the bits of a given 32-bit unsigned integer.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/reverse-bits/
'''


def solution(n):
	'''
	Working inwards from both ends, use bitwise logic to swap each pair of bits.
	'''
	right, left = 0, 31
	while right < left:
		bit_r = n >> right & 1
		bit_l = n >> left & 1

		if bit_r:
			n |= 1 << left
		else:
			n &= ~(1 << left)

		if bit_l:
			n |= 1 << right
		else:
			n &= ~(1 << right)

		right += 1
		left -= 1

	return n
