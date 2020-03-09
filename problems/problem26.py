'''
Blind Curated 75 - Problem 26
=============================

Same Tree
---------

Develop a function that tests whether two binary trees are equal.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/same-tree/
'''


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def solution(p, q):
	'''
	Use recursion.
	'''
	if p and q:
		return p.val == q.val and\
			solution(p.left, q.left) and\
			solution(p.right, q.right)
	return not (p or q)
