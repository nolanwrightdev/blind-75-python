'''
Blind Curated 75 - Problem 37
=============================

Reorder List
------------

Given a singly-linked list _L:
L<sub>0</sub>→L<sub>1</sub>→…→L<sub>n-1</sub>→L<sub>n</sub>_, reorder it to:
_L<sub>0</sub>→L<sub>n</sub>→L<sub>1</sub>→L<sub>n-1</sub>→…_

[→ LeetCode][1]

[1]: https://leetcode.com/problems/reorder-list/
'''


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def solution(head):
	'''
	Save all nodes in an array. Rearrange their `next` pointers as desired.

	An alternative, constant-space approach is possible by 1) finding the midpoint
	of the list, 2) reversing the second half of the list, and 3) interspersing
	each half's nodes.
	'''
	nodes = []

	while head:
		nodes.append(head)
		head = head.next

	if len(nodes) <= 2:
		return nodes[0] if nodes else head

	a, b = 0, len(nodes) - 1
	while a < b:
		nodes[a].next = nodes[b]
		a += 1
		nodes[b].next = nodes[a]
		b -= 1

	nodes[a].next = None
	return nodes[0]
