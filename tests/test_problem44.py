import unittest
from problems.problem44 import solution, ListNode


class Test(unittest.TestCase):
	def test(self):
		dummy = node = ListNode(None)
		for i in [1, 2, 3, 4, 5]:
			node.next = ListNode(i)
			node = node.next
		node = solution(dummy.next)
		for i in [5, 4, 3, 2, 1]:
			self.assertEqual(i, node.val)
			node = node.next
		self.assertIsNone(node)
