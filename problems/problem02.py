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
	While iterating through the input string, maintain 1) a window of adjacent
	characters which are all unique, and 2) a map of characters in the window to
	their positions therein. If a character which already exists in the window
	is encountered, record the size of the window, drop from the window all
	characters up to and including the prior occurence of the encountered
	character, and adjust the map accordingly.
	'''
	max_length = 0
	window = []
	chars_in_window = {}
	for char in s:
		if char in chars_in_window:
			max_length = max(len(window), max_length)
			window = window[chars_in_window[char]:]
			chars_in_window = {}
			for index, char_w in enumerate(window, 1):
				chars_in_window[char_w] = index
		window.append(char)
		chars_in_window[char] = len(window)
	return max(len(window), max_length)
