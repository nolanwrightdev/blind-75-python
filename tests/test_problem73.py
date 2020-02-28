import unittest
from problems.problem73 import TreeNode, solution


class Test(unittest.TestCase):
	def test(self):
		root_s = TreeNode(3)
		root_s.left = TreeNode(4)
		root_s.left.left = TreeNode(1)
		root_s.left.right = TreeNode(2)
		root_s.right = TreeNode(5)
		root_t = TreeNode(4)
		root_t.left = TreeNode(1)
		root_t.right = TreeNode(2)
		self.assertTrue(solution(root_s, root_t))
		root_s = TreeNode(3)
		root_s.left = TreeNode(4)
		root_s.left.left = TreeNode(1)
		root_s.left.right = TreeNode(2)
		root_s.left.right.left = TreeNode(0)
		root_s.right = TreeNode(5)
		root_t = TreeNode(4)
		root_t.left = TreeNode(1)
		root_t.right = TreeNode(2)
		self.assertFalse(solution(root_s, root_t))
		root_s = TreeNode(3)
		root_s.left = TreeNode(4)
		root_s.left.left = TreeNode(1)
		root_s.right = TreeNode(5)
		root_s.right.left = TreeNode(2)
		root_t = TreeNode(3)
		root_t.left = TreeNode(1)
		root_t.right = TreeNode(2)
		self.assertFalse(solution(root_s, root_t))
