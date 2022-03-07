# -*- coding: utf-8 -*-
"""
H-Index
https://programmers.co.kr/learn/courses/30/lessons/42747
"""

def solution(citations):
	citations.sort(reverse=True)
	for i in range(len(citations), -1, -1):
		if i == 0:
			return 0
		# print(i)
		# print(citations[:i])
		if min(citations[:i]) >= i:
			return i
	# answer = 0
	# return answer

print(solution([0, 0, 0, 1, 0]))