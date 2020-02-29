'''
Blind Curated 75 - Problem 72
=============================

Palindromic Substrings
----------------------

Count the number of palindromic substrings exist which exist in a given string.
Substrings which consist of the same characters but which start or end at
different points should be counted as distinct substrings.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/palindromic-substrings/
'''


def solution(s):
	'''
	Begin with all the centers of possible palindromes. Expanding outward from the
	centers, a string is a palindrome if the leftmost and rightmost characters are
	the same.
	'''
	count = len(s)
	under_consideration = []
	for i in range(1, len(s)):
		under_consideration.append([i - 1, i])
	for i in range(2, len(s)):
		under_consideration.append([i - 2, i])
	while under_consideration:
		left, right = under_consideration.pop()
		if s[left] == s[right]:
			count += 1
			if 0 <= left - 1 and right + 1 < len(s):
				under_consideration.append([left - 1, right + 1])
	return count
