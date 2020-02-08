'''
Blind Curated 75 - Problem 24
=============================

Decode Ways
-----------

A message containing letters _A_ through _Z_ is encoded such that each letter is
replaced with its ordinal position in the alphabet. Given such a message,
determine the number of possible ways to decode it.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/decode-ways/
'''


def solution(s):
	'''
	This is a bottom-up dynamic programming solution. The idea is that the number
	of ways a string of length _n_ can be decoded is equal to the number of ways
	that same string minus the last character can be decoded plus the number of
	ways that string minus the last two characters can be decoded, provided the
	characters left off are valid themselves.
	'''
	w = [1, int(bool(int(s[0])))]
	for i in range(1, len(s)):
		l2, l1 = int(s[i - 1:i + 1]), int(s[i])
		w[0], w[1] = w[1], w[0] * (9 < l2 <= 26) + w[1] * bool(l1)
		if not w[1]:
			break
	return w[1]
