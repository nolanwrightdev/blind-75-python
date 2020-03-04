import unittest
from problems.problem29 import TreeNode, solution


class Test(unittest.TestCase):
	def test(self):
		root = solution([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
		self.assertEqual(root.val, 3)
		self.assertEqual(root.left.val, 9)
		self.assertEqual(root.right.val, 20)
		self.assertEqual(root.right.left.val, 15)
		self.assertEqual(root.right.right.val, 7)
