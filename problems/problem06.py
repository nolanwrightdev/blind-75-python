'''
Blind Curated 75 - Problem 06
=============================

Remove Nth Node From End of List
--------------------------------

Given a linked list, remove the nth node from the end of the list and return its
head.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def solution(head, n):
	'''
	Save each node of the linked list in an array. Index into the array to remove
	the required node.
	'''
	nodes = []
	while head is not None:
		nodes.append(head)
		head = head.next
	if n == 1:
		if len(nodes) == 1:
			return None
		nodes[-2].next = None
	elif n == len(nodes):
		return nodes[1]
	else:
		nodes[-n-1].next = nodes[-n+1]
	return nodes[0]
