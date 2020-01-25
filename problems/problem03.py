'''
Blind Curated 75 - Problem 03
=============================

Longest Palindromic Substring
-----------------------------

Find the longest palindromic substring in a given string.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/longest-palindromic-substring/
'''


def solution(s):
	'''
	Iterate through all possible centers of palindromes. For each, expand one unit
	outward from the center so long as the sequence remains a palindrome. Record
	the longest such palindrome.
	'''
	longest = s if len(s) <= 1 else ''
	for i in range(len(s) - 1):
		for left, right in (i, i), (i, i + 1):
			while left >= 0 and right < len(s) and s[left] == s[right]:
				left -= 1
				right += 1
			if abs(right - left) - 1 > len(longest):
				longest = s[left + 1:right]
	return longest
