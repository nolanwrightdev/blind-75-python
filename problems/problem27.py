'''
Blind Curated 75 - Problem 27
=============================

Binary Tree Level Order Traversal
---------------------------------

Given a binary tree, return the level-order traversal of its nodes' values (from
left to right, level by level).

[→ LeetCode][1]

[1]: https://leetcode.com/problems/binary-tree-level-order-traversal/
'''


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def solution(root):
	'''
	Use a queue. Operate on all the nodes in the queue in order. Replenish
	the queue with all the nodes' children and repeat the cycle.
	'''
	if not root:
		return []

	levels, level = [], [root]

	while level:
		next_level = []

		for node in level:
			if node.left:
				next_level.append(node.left)
			if node.right:
				next_level.append(node.right)

		levels.append([node.val for node in level])
		level = next_level

	return levels
