import unittest
from problems.problem36 import solution, ListNode


class Test(unittest.TestCase):
	def test(self):
		head1 = ListNode(3)
		loop1 = ListNode(2)
		head1.next = loop1
		head1.next.next = ListNode(0)
		head1.next.next.next = ListNode(-4)
		head1.next.next.next.next = loop1
		self.assertTrue(solution(head1))
		head2 = ListNode(1)
		head2.next = ListNode(2)
		head2.next.next = head2
		self.assertTrue(solution(head2))
		self.assertFalse(solution(ListNode(1)))
