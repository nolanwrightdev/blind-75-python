'''
Blind Curated 75 - Problem 29
=============================

Construct Binary Tree from Preorder and Inorder Traversal
---------------------------------------------------------

Construct a binary tree from its preorder and inorder traversals. Assume no
duplicates exist in the tree.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
'''


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def solution(preorder, inorder):
	'''
	A key point to note is that the preorder traversal's first element is always
	the root element. Furthermore, in the preorder traversal, all of the left side
	of the tree's elements precede any of the right side of the tree's elements.
	The left side of the tree's elements can be distinguished from the right side
	of the tree's elements as they will precede the root element in the inorder
	traversal, while the right side of the tree's elements will follow the root
	element in the inorder traversal.
	'''
	return recurse(preorder[::-1], inorder)


def recurse(preorder, inorder):
	if not preorder or not inorder:
		return None

	root = TreeNode(preorder.pop())
	index = inorder.index(root.val)
	root.left = recurse(preorder, inorder[:index])
	root.right = recurse(preorder, inorder[index+1:])
	return root
