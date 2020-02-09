'''
Blind Curated 75 - Problem 36
=============================

Linked List Cycle
-----------------

Given a linked list, determine if it has a cycle in it.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/linked-list-cycle/
'''


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def solution(head):
	'''
	Maintain two pointers, one of which advances at twice the rate of the other.
	If at any time the two pointers are pointing to the same node, then there is a
	a loop. If, on the other hand, the faster pointer reaches the end of the list,
	then there is not a loop.
	'''
	p1 = p2 = head
	while p2:
		p1 = p1.next
		p2 = p2.next
		if p2:
			p2 = p2.next
		else:
			break
		if p1 is p2:
			return True
	return False
