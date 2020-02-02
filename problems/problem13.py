'''
Blind Curated 75 - Problem 13
=============================

Group Anagrams
-----------------

Given an array of strings, group anagrams together.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/group-anagrams/
'''


def solution(strs):
	'''
	Assume all strings are composed solely of characters which are in the English
	alphabet and are lower case. For each string, initialize an array of length
	twenty-six and use it to count the frequencies of each character. Use a hash
	map to collect anagrams by common frequencies.
	'''
	anagrams = {}
	for s in strs:
		characters = [0] * 26
		for char in s:
			characters[ord(char) - ord('a')] += 1
		tup = tuple(characters)
		anagrams[tup] = anagrams.get(tup, []) + [s]
	return anagrams.values()
