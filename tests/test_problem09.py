import unittest
from problems.problem09 import solution, ListNode


class Test(unittest.TestCase):
	def test(self):
		a = None
		for i in 5, 4, 1:
			node = ListNode(i)
			node.next = a
			a = node
		b = None
		for i in 4, 3, 1:
			node = ListNode(i)
			node.next = b
			b = node
		c = None
		for i in 6, 2:
			node = ListNode(i)
			node.next = c
			c = node
		ret = solution([a, b, c])
		for i in 1, 1, 2, 3, 4, 4, 5, 6:
			self.assertEqual(ret.val, i)
			ret = ret.next
		self.assertIsNone(ret)
