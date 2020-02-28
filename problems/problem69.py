'''
Blind Curated 75 - Problem 69
=============================

Sum of Two Integers
-------------------

Calculate the sum of two integers without using the `+` or `-` operators.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/sum-of-two-integers/
'''


def solution(a, b):
	'''
	Python represents numbers internally with an "infinite" number of bits;
	however this function assumes the numbers are composed only of 32 bits and
	thus masks them off at that point. It is possible to add two numbers using
	two bitwise operations. With the `^` (XOR) operator, combine the set bits of
	the two numbers. Corresponding bits which are both set result in a carry over
	to the next most-significant bit. The carry bits can be found with the `&`
	(AND) operator. Continue performing the above operations with the result of
	the `^` operation and the result of the `&` operation, shifted to the left by
	one bit, until the carry bits are all zero. If the resulting non-zero number
	has its most-signficant bit set, then it is negative, and it must be
	reformatted to abide by Python's internal representation. This can be achieved
	by flipping the 32 least-significant bits and then flipping all of the
	"infinite" bits which Python uses internally to represent the number.
	'''
	mask = 0xffffffff
	while b:
		a, b = (a ^ b) & mask, ((a & b) << 1) & mask
	return a if a < 0x80000000 else ~(a ^ mask)
