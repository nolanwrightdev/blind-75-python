'''
Blind Curated 75 - Problem 45
=============================

Course Schedule
---------------

There are a total of _n_ courses you have to take, labeled from `0` to `n - 1`.
Some courses have prerequisites. For example, to take course 0, you might first
have to take course 1, which is expressed as the pair: `[0, 1]`.

Given the total number of courses and a list of prerequisite pairs, determine
whether it is possible for you to finish all _n_ courses.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/maximum-product-subarray/
'''


def solution(num_courses, prerequisites):
	'''
	Perform depth-first searches through the chains of prerequisites. If, while
	searching, a node already encountered in the search is encountered again, then
	there exists a cycle, which means it is not possible to finish all courses.
	'''
	courses = [[] for _ in range(num_courses)]

	for course, prereq in prerequisites:
		courses[course].append(prereq)

	visited = [False for _ in range(num_courses)]
	for course in range(num_courses):
		if not visited[course]:
			traversal = [False for _ in range(num_courses)]
			stack = [(course, False)]
			while stack:
				course, backtracking = stack.pop()
				if not visited[course]:
					if backtracking:
						traversal[course] = False
						visited[course] = True
					else:
						if traversal[course]:
							return False
						traversal[course] = True
						stack.append((course, True))
						stack.extend(
						    (prereq, False) for prereq in courses[course])

	return True
