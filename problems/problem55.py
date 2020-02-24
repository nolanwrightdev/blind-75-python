'''
Blind Curated 75 - Problem 55
=============================

Valid Anagram
-------------

Develop a function to find whether two strings are anagrams. Assume the strings
are composed only of lower case English letters.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/valid-anagram/
'''


def solution(s, t):
	'''
	Make sure all the letters in both words have the same frequencies.
	'''
	if len(s) != len(t):
		return False

	sc = [0] * 26
	tc = [0] * 26
	for i in range(len(s)):
		sc[ord(s[i]) - ord('a')] += 1
		tc[ord(t[i]) - ord('a')] += 1

	return all(a == b for a, b in zip(sc, tc))
