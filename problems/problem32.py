'''
Blind Curated 75 - Problem 32
=============================

Valid Palindrome
----------------

Given a string, determine whether it is a palindrome, considering only
alphanumeric characters and ignoring case.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/valid-palindrome/
'''


def solution(s):
	'''
	Move inward from the ends, checking at each step that the characters on either
	end are valid and equal.
	'''
	left, right = 0, len(s) - 1
	while left < right:
		if not s[left].isalnum():
			left += 1
		elif not s[right].isalnum():
			right -= 1
		elif s[left].lower() != s[right].lower():
			return False
		else:
			left += 1
			right -= 1
	return True
