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
	Find the indices of all characters in the string. For each character, use the
	sliding window technique with its indices to find the length of the longest
	substring matching the desired criteria.
	'''
	if k >= len(s):
		return len(s)

	cps = [[] for _ in range(26)]
	for i, char in enumerate(s):
		cps[ord(char) - ord('A')].append(i)

	longest = k
	for cp in cps:
		if not cp:
			continue

		left = right = 0
		kloop = k
		length = 1
		while right < len(cp):
			while right + 1 < len(cp) and\
               cp[right + 1] - cp[right] - 1 <= kloop:
				kloop -= cp[right + 1] - cp[right] - 1
				length += cp[right + 1] - cp[right]
				right += 1

			longest = max(longest, length + kloop)
			if right == len(cp) - 1:
				break

			while left < right and cp[right + 1] - cp[right] - 1 > kloop:
				kloop += cp[left + 1] - cp[left] - 1
				length -= cp[left + 1] - cp[left]
				left += 1

			if left == right:
				left = right = right + 1

	return min(longest, len(s))
