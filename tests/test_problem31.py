import unittest
from problems.problem31 import TreeNode, Solution


class Test(unittest.TestCase):
	def test(self):
		solution = Solution()
		root = TreeNode(1)
		root.left = TreeNode(2)
		root.right = TreeNode(3)
		self.assertEqual(solution.max_path_sum(root), 6)
		root = TreeNode(-10)
		root.left = TreeNode(9)
		root.right = TreeNode(20)
		root.right.left = TreeNode(15)
		root.right.right = TreeNode(7)
		self.assertEqual(solution.max_path_sum(root), 42)
