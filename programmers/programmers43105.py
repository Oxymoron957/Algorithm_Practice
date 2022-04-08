# -*- coding: utf-8 -*-
"""
정수 삼각형
https://programmers.co.kr/learn/courses/30/lessons/43105
"""

def solution(triangle):
	cur_idx = 0
	sums = triangle[0][0]

	if len(triangle) == 1:
		return triangle[0][0]

	for i in range(1, len(triangle)-1):
		if triangle[i][cur_idx] + max([triangle[i+1][cur_idx], triangle[i+1][cur_idx+1]]) > triangle[i][cur_idx+1] + max([triangle[i+1][cur_idx+1], triangle[i+1][cur_idx+2]]):
			sums += triangle[i][cur_idx]
		else:
			sums += triangle[i][cur_idx+1]
			cur_idx += 1
	sums += max([triangle[len(triangle)-1][cur_idx], triangle[len(triangle)-1][cur_idx+1]])

	return sums

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 50]]))
print(solution([[7]]))
