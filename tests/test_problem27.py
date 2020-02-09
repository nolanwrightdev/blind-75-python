import unittest
from problems.problem27 import solution, TreeNode


class Test(unittest.TestCase):
	def test(self):
		root = TreeNode(3)
		root.left = TreeNode(9)
		root.right = TreeNode(20)
		root.right.left = TreeNode(15)
		root.right.right = TreeNode(7)
		res = solution(root)
		answer = [[3], [9, 20], [15, 7]]
		self.assertEqual(len(res), len(answer))
		for i in zip(res, answer):
			self.assertListEqual(*i)
