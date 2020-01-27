'''
Blind Curated 75 - Problem 09
=============================

Merge k Sorted Lists
--------------------

Merge _k_ sorted linked lists and return it as one sorted list.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/merge-k-sorted-lists/
'''

import heapq


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def __eq__(self, o):
		return self.val == o.val

	def __lt__(self, o):
		return self.val < o.val

	def __le__(self, o):
		return self.val <= o.val


def solution(lists):
	'''
	Form the list of linked lists into a min heap. Pop off the minimum-value list.
	Append to the return list while this list's nodes are lesser than the new
	minimum-value list. Push the list back onto the heap. Repeat the process until
	all lists are exhausted.
	'''
	lists = [l for l in lists if l]
	heapq.heapify(lists)
	dummy = cur = ListNode(None)
	while lists:
		node = heapq.heappop(lists)
		if not lists:
			cur.next = node
			break
		while node <= lists[0]:
			cur.next = node
			cur = node
			node = node.next
			if not node:
				break
		if node:
			heapq.heappush(lists, node)
	return dummy.next
