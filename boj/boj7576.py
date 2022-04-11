# -*- coding: utf-8 -*-
"""
토마토
https://www.acmicpc.net/problem/7576
"""

from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())
maps = []
for _ in range(N):
	maps.append(list(map(int, input().split())))


queue = deque()

for y in range(N):
	for x in range(M):
		if maps[y][x] == 1:
			queue.append([y, x])

while queue:
	y, x = queue.popleft()

	for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
		ny = y + dy
		nx = x + dx

		if 0 <= ny < N and 0 <= nx < M and maps[ny][nx] == 0:
			maps[ny][nx] = maps[y][x] + 1
			queue.append([ny, nx])

riped = True
for y in range(N):
	for x in range(M):
		if maps[y][x] == 0:
			riped = False

if riped:
	print(max(map(max, maps))-1)
else:
	print(-1)
