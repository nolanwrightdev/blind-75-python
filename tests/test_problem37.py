import unittest
from problems.problem37 import solution, ListNode


class Test(unittest.TestCase):
	def test(self):
		dummy = node = ListNode(None)
		for i in [1, 2, 3, 4]:
			node.next = ListNode(i)
			node = node.next
		solution(dummy.next)
		node = dummy.next
		for i in [1, 4, 2, 3]:
			self.assertEqual(i, node.val)
			node = node.next
		self.assertIsNone(node)
		node = dummy
		for i in [1, 2, 3, 4, 5]:
			node.next = ListNode(i)
			node = node.next
		solution(dummy.next)
		node = dummy.next
		for i in [1, 5, 2, 4, 3]:
			self.assertEqual(i, node.val)
			node = node.next
		self.assertIsNone(node)
