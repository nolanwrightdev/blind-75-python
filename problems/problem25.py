'''
Blind Curated 75 - Problem 25
=============================

Validate Binary Search Tree
---------------------------

Given a binary tree, determine if it is a valid binary search tree.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/validate-binary-search-tree/
'''


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def solution(root):
	'''
	Recurse through the tree while maintaining lower and upper bounds. Each node's
	value must fall within the valid range.
	'''
	if not root:
		return True

	def recurse(node, left_bound, right_bound):
		if not node:
			return True

		if not left_bound < node.val < right_bound:
			return False

		return recurse(node.left, left_bound, node.val) and \
         recurse(node.right, node.val, right_bound)


	return recurse(root.left, float('-inf'), root.val) and \
     recurse(root.right, root.val, float('inf'))
