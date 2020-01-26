import unittest
from problems.problem06 import solution, ListNode


class Test(unittest.TestCase):
	def test(self):
		last = None
		for i in range(5, 0, -1):
			node = ListNode(i)
			node.next = last
			last = node
		head = solution(last, 2)
		for i in 1, 2, 3, 5:
			self.assertEqual(i, head.val)
			head = head.next
		self.assertIsNone(head)
		self.assertIsNone(solution(ListNode(1), 1))
