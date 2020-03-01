'''
Blind Curated 75 - Problem 71
=============================

Longest Repeating Character Replacement
---------------------------------------

Given a string `s` that consists of only uppercase English letters, you can
perform at most `k` operations on that string.

In one operation, you may choose any character of the string and change it to
any other uppercase English character.

Find the length of the longest substring containing all repeating letters which
can be found after performing the operations.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/longest-repeating-character-replacement/
'''


def solution(s, k):
	'''
	Use the sliding window technique. While keeping track of the frequency of the
	most frequent character, expand the window as much as possible. If the window
	becomes invalid, slide it over until it is once again valid and continue
	expanding while it remains valid.
	'''
	max_length = 0
	max_count = 0
	counts = [0] * 26
	start = 0
	for end in range(len(s)):
		ind = ord(s[end]) - ord('A')
		counts[ind] += 1
		max_count = max(max_count, counts[ind])
		if end - start + 1 - max_count > k:
			counts[ord(s[start]) - ord('A')] -= 1
			start += 1
		else:
			max_length = max(max_length, end - start + 1)
	return max_length
