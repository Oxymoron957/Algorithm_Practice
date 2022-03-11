# -*- coding: utf-8 -*-
"""
안전 영역
https://www.acmicpc.net/problem/2468
"""

from collections import deque

N = int(input())
board = []
for i in range(N):
	board.append(list(map(int, input().split())))

di = [1, -1, 0, 0]
dj = [0, 0 , 1, -1]

answer = 0
for cur_level in range(min(map(min, board))-1, max(map(max, board))+1):
	cnt = 0 # 안전지대의 갯수 
	visited = [[False]*N for _ in range(N)]
	for i in range(N):
		for j in range(N):
			if visited[i][j] == True or board[i][j] <= cur_level:
				continue
			cnt += 1
			dq = deque()
			dq.append([i, j])
			visited[i][j] = True
		
			while dq:
				ci, cj = dq.popleft()
				for _ in range(4):
					ni = ci + di[_]
					nj = cj + dj[_]

					if 0 <= ni <= N-1 and 0 <= nj <= N-1:
						if visited[ni][nj] == False and board[ni][nj] > cur_level:
							dq.append([ni, nj])
							visited[ni][nj] = True
	if cnt > answer:
		answer = cnt

print(answer)


