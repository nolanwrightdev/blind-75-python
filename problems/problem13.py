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
	Sort each string. Find the frequencies of each character in each string. Use a
	hash map to collect anagrams by common frequencies.
	'''
	anagrams = {}
	for s in strs:
		chars, i, frequencies = sorted(s), 0, []
		while i < len(chars):
			j = i + 1
			while j < len(chars) and chars[j] == chars[i]:
				j += 1
			frequencies += [chars[i], j - i]
			i = j
		tup = tuple(frequencies)
		lst = anagrams.get(tup, [])
		lst.append(s)
		anagrams[tup] = lst
	return anagrams.values()
