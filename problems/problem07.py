'''
Blind Curated 75 - Problem 07
=============================

Valid Parentheses
-----------------

Given a string containing just the characters `(`, `)`, '{', '}', '[' and ']',
determine if the input string is valid.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/valid-parentheses/
'''

def solution(s):
	'''
	Ensure the first character is an opening delimeter. Find the closing delimiter
	which corresponds to this first character. It may not be the very next closing
	delimiter of its sort. Once the match is found, recurse on the parts of the
	string which exist within the matching delimiters and to the right of them.
	'''
	if not s:
		return True
	if len(s) % 2 or s[0] not in '({[':
		return False
	count = 0
	closing = {'(': ')', '{': '}', '[': ']'}[s[0]]
	for i, delimiter in enumerate(s[1:], 1):
		if delimiter == s[0]:
			count += 1
		if delimiter == closing:
			if count == 0:
				return solution(s[1:i]) and (i == len(s) - 1 or solution(s[i+1:]))
			count -= 1
			if c < 0:
				break
	return False
