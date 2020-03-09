import unittest
from problems.problem28 import solution, TreeNode


class Test(unittest.TestCase):
	def test(self):
		root = TreeNode(3)
		root.left = TreeNode(9)
		root.right = TreeNode(20)
		root.right.left = TreeNode(15)
		root.right.right = TreeNode(7)
		self.assertEqual(solution(root), 3)
