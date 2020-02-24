import unittest
from problems.problem52 import TreeNode, solution


class Test(unittest.TestCase):
	def test(self):
		root = TreeNode(3)
		root.left = TreeNode(1)
		root.left.right = TreeNode(2)
		root.right = TreeNode(4)
		self.assertEqual(solution(root, 1), 1)
		root = TreeNode(5)
		root.left = TreeNode(3)
		root.left.left = TreeNode(2)
		root.left.left.left = TreeNode(1)
		root.left.right = TreeNode(4)
		root.right = TreeNode(6)
		self.assertEqual(solution(root, 3), 3)
