import unittest
from problems.problem08 import solution, ListNode


class Test(unittest.TestCase):
	def test(self):
		l1 = None
		for i in 4, 2, 1:
			node = ListNode(i)
			node.next = l1
			l1 = node
		l2 = None
		for i in 4, 3, 1:
			node = ListNode(i)
			node.next = l2
			l2 = node
		ret = solution(l1, l2)
		for i in 1, 1, 2, 3, 4, 4:
			self.assertEqual(ret.val, i)
			ret = ret.next
		self.assertIsNone(ret)
