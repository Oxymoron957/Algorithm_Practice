# -*- coding: utf-8 -*-
"""
카펫
https://programmers.co.kr/learn/courses/30/lessons/42842
"""

def solution(brown, yellow):
	x = 3
	y = (brown+4)/2 - x

	while x*y != brown+yellow:
		x += 1
		y = (brown+4)/2 - x
	return [y,x]

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
