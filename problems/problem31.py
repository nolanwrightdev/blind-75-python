'''
Blind Curated 75 - Problem 31
=============================

Binary Tree Maximum Path Sum
----------------------------

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting
node to any node in the tree along the parent-child connections. The path must
contain at least one node and does not need to go through the root.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	'''
	Recurse over the tree. For a given node, first calculate the maximum paths
	through either of its children. Since the maximum path may branch across both
	the left and right children, record the the maximum path at each step, but
	only return to the parent the longer of the two branches.
	'''
	def max_path_sum(self, root):
		self.max_sum = float('-inf')
		self.recurse(root)
		return self.max_sum

	def recurse(self, node):
		if not node:
			return 0
		left = self.recurse(node.left)
		right = self.recurse(node.right)
		self.max_sum = max(self.max_sum,
		                   max(left, 0) + node.val + max(right, 0))
		return max(left, right, 0) + node.val
