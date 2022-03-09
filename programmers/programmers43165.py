# -*- coding: utf-8 -*-
"""
타겟 넘버
https://programmers.co.kr/learn/courses/30/lessons/43165
"""

from collections import deque

def solution(numbers, target):

	dq = deque()
	dq.append([numbers[0], 1, [numbers[0]]])
	dq.append([-1*numbers[0], 1, [numbers[0]]])

	answer = 0
	while dq:
		val, level, li = dq.popleft()
		if level == len(numbers) and val == target:
			# print(li)
			answer += 1
		if level < len(numbers):
			dq.append([val+numbers[level], level+1, li + [numbers[level]]])
			dq.append([val-numbers[level], level+1, li + [-1*numbers[level]]])
	return answer

print(solution([1, 1, 1, 1, 1], 3))
# print(solution([4, 1, 2, 1], 4))