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
	Push opening delimiters onto a stack while iterating through the input string.
	When a closing delimiter is encountered, pop a delimiter off the stack and
	ensure it matches the closing one. The input string is valid if the stack is
	empty after completely iterating through the input string.
	'''
	if not s:
		return True
	if len(s) % 2 or s[0] in ')}]' or s[-1] in '({[':
		return False
	stack = []
	for delimiter in s:
		if delimiter in '({[':
			stack.append(delimiter)
		elif not stack or stack.pop() != {
		    ')': '(',
		    '}': '{',
		    ']': '['
		}[delimiter]:
			return False
	return not stack
