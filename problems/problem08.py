'''
Blind Curated 75 - Problem 08
=============================

Merge Two Sorted Lists
----------------------

Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/merge-two-sorted-lists/
'''


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def solution(l1, l2):
	'''
	Move along both linked lists, comparing the nodes at each point and linking
	the lesser of the two to the return list.
	'''
	dummy = ret = ListNode(None)
	while l1 and l2:
		if l1.val < l2.val:
			ret.next = l1
			ret = l1
			l1 = l1.next
		else:
			ret.next = l2
			ret = l2
			l2 = l2.next
	ret.next = l1 if l1 else l2
	return dummy.next
