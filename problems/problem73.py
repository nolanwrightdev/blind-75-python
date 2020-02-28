'''
Blind Curated 75 - Problem 73
=============================

Subtree of Another Tree
-----------------------

Given two non-empty binary trees **s** and **t**, find whether tree **t** has
exactly the same structure and node values as some subtree of **s**. Note that
**s** may be considered a subtree of itself.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/subtree-of-another-tree/
'''


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def eq(a, b):
	if a and b:
		return a.val == b.val and eq(a.left, b.left) and eq(a.right, b.right)
	return not a and not b


def solution(s, t):
	'''
	If **s** and **t** are identical, return `True`. Otherwise check whether **t**
	is identical to a subtree of **s**.
	'''
	if not s:
		return False
	return eq(s, t) or solution(s.left, t) or solution(s.right, t)
