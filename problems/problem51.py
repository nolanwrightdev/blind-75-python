'''
Blind Curated 75 - Problem 51
=============================

Invert Binary Tree
------------------

Invert a binary tree.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/invert-binary-tree/
'''


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def solution(root):
	'''
	Recursively swap left and right nodes.
	'''
	if root:
		root.left, root.right = root.right, root.left
		solution(root.left)
		solution(root.right)
	return root
