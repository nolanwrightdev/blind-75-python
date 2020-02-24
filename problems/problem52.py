'''
Blind Curated 75 - Problem 52
=============================

Kth Smallest Element in a BST
-----------------------------

Given a binary search tree, develop a function to find the **k**th smallest
element therein.

Assume _k_ is always valid.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
'''


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def solution(root, k):
	'''
	Perform an in-order traversal until the **k**th smallest element is reached.
	'''
	stack = []
	while True:
		if root:
			stack.append(root)
			root = root.left
		else:
			node = stack.pop()
			k -= 1
			if k == 0:
				return node.val
			root = node.right
