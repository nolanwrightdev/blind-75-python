import unittest
from problems.problem26 import solution, TreeNode


class Test(unittest.TestCase):
	def test(self):
		root1 = TreeNode(1)
		root1.left = TreeNode(2)
		root1.right = TreeNode(3)
		root2 = TreeNode(1)
		root2.left = TreeNode(2)
		root2.right = TreeNode(3)
		self.assertTrue(solution(root1, root2))
		root1 = TreeNode(1)
		root1.left = TreeNode(2)
		root2 = TreeNode(1)
		root2.right = TreeNode(2)
		self.assertFalse(solution(root1, root2))
		root1 = TreeNode(1)
		root1.left = TreeNode(2)
		root1.right = TreeNode(1)
		root2 = TreeNode(1)
		root2.left = TreeNode(1)
		root2.right = TreeNode(2)
		self.assertFalse(solution(root1, root2))
