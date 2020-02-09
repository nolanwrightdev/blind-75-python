import unittest
from problems.problem25 import solution, TreeNode


class Test(unittest.TestCase):
	def test(self):
		root1 = TreeNode(2)
		root1.left = TreeNode(1)
		root1.right = TreeNode(3)
		self.assertTrue(solution(root1))
		root2 = TreeNode(5)
		root2.left = TreeNode(1)
		root2.right = TreeNode(4)
		root2.right.left = TreeNode(3)
		root2.right.right = TreeNode(6)
		self.assertFalse(solution(root2))
		root3 = TreeNode(10)
		root3.left = TreeNode(5)
		root3.right = TreeNode(15)
		root3.right.left = TreeNode(6)
		root3.right.right = TreeNode(20)
		self.assertFalse(solution(root3))
