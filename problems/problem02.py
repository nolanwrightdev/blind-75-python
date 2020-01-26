'''
Blind Curated 75 - Problem 02
=============================

Longest Substring Without Repeating Characters
----------------------------------------------

Given a string, find the length of the longest substring without repeating
characters.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''


def solution(s):
	'''
	While iterating through the input string, maintain 1) a starting index since
	which no duplicate characters have been encountered, and 2) a map of
	characters to their most-recently encountered indices in the input string. If
	a character is encountered which already exists in the map and whose
	most-recent index occurs after the starting index, record the number of
	characters from the starting index to this character's index, and update the
	starting index to be one after the character's last occurence.
	'''
	max_length = 0
	start = 0
	char_pos = {}
	for pos, char in enumerate(s):
		last = char_pos.get(char, -1)
		if last >= start:
			max_length = max(max_length, pos - start)
			start = last + 1
		char_pos[char] = pos
	return max(max_length, len(s) - start)
