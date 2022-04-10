# -*- coding: utf-8 -*-
"""
파이프 옮기기 1
https://www.acmicpc.net/problem/17070
"""

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
maps = []
for _ in range(N):
	maps.append(list(map(int, input().split())))

dq = deque()
dq.append([[0, 0], [0, 1]])

answer = 0

def inboundary(x, y):
	global N
	if 0 <= x <= N-1 and 0 <= y <= N-1:
		return True
	else:
		return False

while dq:
	cur_head, cur_tail = dq.pop()
	
	if cur_tail == [N-1, N-1]:
		answer += 1
		continue

	# 가로 상태일 때
	if cur_head[0] == cur_tail[0] and cur_head[1] == cur_tail[1]-1:
		if inboundary(cur_tail[0], cur_tail[1]+1) and maps[cur_tail[0]][cur_tail[1]+1] != 1:
			dq.append([[cur_head[0], cur_head[1]+1], [cur_tail[0], cur_tail[1]+1]])
		if inboundary(cur_tail[0], cur_tail[1]+1) and inboundary(cur_tail[0]+1, cur_tail[1]) and inboundary(cur_tail[0]+1, cur_tail[1]+1) and maps[cur_tail[0]][cur_tail[1]+1] != 1 and maps[cur_tail[0]+1][cur_tail[1]] != 1 and maps[cur_tail[0]+1][cur_tail[1]+1] != 1:
			dq.append([[cur_head[0], cur_head[1]+1], [cur_tail[0]+1, cur_tail[1]+1]])
	# 세로 상태일 때
	if cur_head[1] == cur_tail[1] and cur_head[0] == cur_tail[0]-1:
		if inboundary(cur_tail[0]+1, cur_tail[1]) and maps[cur_tail[0]+1][cur_tail[1]] != 1:
			dq.append([[cur_head[0]+1, cur_head[1]], [cur_tail[0]+1, cur_tail[1]]])
		if inboundary(cur_tail[0], cur_tail[1]+1) and inboundary(cur_tail[0]+1, cur_tail[1]) and inboundary(cur_tail[0]+1, cur_tail[1]+1) and maps[cur_tail[0]][cur_tail[1]+1] != 1 and maps[cur_tail[0]+1][cur_tail[1]] != 1 and maps[cur_tail[0]+1][cur_tail[1]+1] != 1:
			dq.append([[cur_head[0]+1, cur_head[1]], [cur_tail[0]+1, cur_tail[1]+1]])
	# 가로 상태일 때
	if cur_head[0] == cur_tail[0]-1 and cur_head[1] == cur_tail[1]-1:
		if inboundary(cur_tail[0], cur_tail[1]+1) and maps[cur_tail[0]][cur_tail[1]+1] != 1:
			dq.append([[cur_head[0]+1, cur_head[1]+1], [cur_tail[0], cur_tail[1]+1]])
		if inboundary(cur_tail[0]+1, cur_tail[1]) and maps[cur_tail[0]+1][cur_tail[1]] != 1:
			dq.append([[cur_head[0]+1, cur_head[1]+1], [cur_tail[0]+1, cur_tail[1]]])
		if inboundary(cur_tail[0], cur_tail[1]+1) and inboundary(cur_tail[0]+1, cur_tail[1]) and inboundary(cur_tail[0]+1, cur_tail[1]+1) and maps[cur_tail[0]][cur_tail[1]+1] != 1 and maps[cur_tail[0]+1][cur_tail[1]] != 1 and maps[cur_tail[0]+1][cur_tail[1]+1] != 1:
			dq.append([[cur_head[0]+1, cur_head[1]+1], [cur_tail[0]+1, cur_tail[1]+1]])
		
print(answer)