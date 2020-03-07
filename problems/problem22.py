'''
Blind Curated 75 - Problem 22
=============================

Minimum Window Substring
------------------------

Given a string S and a string T, find the minimum window in S which contains all
the characters in T. The time complexity of the solution should not exceed O(n).

[→ LeetCode][1]

[1]: https://leetcode.com/problems/minimum-window-substring/
'''

import collections


def solution(s, t):
	'''
	Use the sliding window technique. Expand the window until it contains all the
	required characters. Then contract it until it is no longer valid. Repeat
	until the window has expanded to the end of the given string.
	'''
	counts = collections.Counter(t)
	counter = collections.Counter()
	counted = left = right = 0
	min_substr = s + '#'

	while right < len(s):
		while right < len(s) and counted < len(counts):
			if s[right] in counts:
				counter[s[right]] += 1
				if counter[s[right]] == counts[s[right]]:
					counted += 1
			right += 1

		while counted == len(counts):
			if s[left] in counter:
				counter[s[left]] -= 1
				if counter[s[left]] < counts[s[left]]:
					counted -= 1
					if right - left < len(min_substr):
						min_substr = s[left:right]
			left += 1

	return min_substr if len(min_substr) <= len(s) else ''
