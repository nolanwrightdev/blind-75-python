'''
Blind Curated 75 - Problem 44
=============================

Reverse Linked List
-------------------

Reverse a singly-linked list.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/reverse-linked-list/
'''


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def solution(head):
	'''
	Rearrange each node's pointer to point to the previous node.
	'''
	last = None
	while head:
		temp = head.next
		head.next = last
		last = head
		head = temp
	return last
