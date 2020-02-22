import unittest
from problems.problem51 import TreeNode, solution


class Test(unittest.TestCase):
	def test(self):
		root = TreeNode(4)
		root.left = TreeNode(2)
		root.left.left = TreeNode(1)
		root.left.right = TreeNode(3)
		root.right = TreeNode(7)
		root.right.left = TreeNode(6)
		root.right.right = TreeNode(9)
		root = solution(root)
		self.assertEqual(root.val, 4)
		self.assertEqual(root.left.val, 7)
		self.assertEqual(root.left.left.val, 9)
		self.assertEqual(root.left.right.val, 6)
		self.assertEqual(root.right.val, 2)
		self.assertEqual(root.right.left.val, 3)
		self.assertEqual(root.right.right.val, 1)
