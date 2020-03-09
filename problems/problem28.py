'''
Blind Curated 75 - Problem 28
=============================

Maximum Depth of Binary Tree
----------------------------

Develop a function to find the maximum depth of a binary tree.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def solution(root):
	'''
	Use recursion.
	'''
	return 1 + max(solution(root.left), solution(root.right)) if root else 0
