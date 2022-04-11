# -*- coding: utf-8 -*-
"""
개똥벌레
https://www.acmicpc.net/problem/3020
"""

from collections import deque
import sys
input = sys.stdin.readline

N, H = map(int, input().split())

down = deque()
up = deque()

for _ in range(int(N/2)):
	down.append(int(input()))
	up.append(int(input()))

levels = [0 for _ in range(H)]
while down:
	d = down.pop()
	u = up.pop()

	for i in range(0, d):
		levels[i] += 1
	for i in range(u+1, N+1):
		levels[i] += 1

print(min(levels), len(list(filter(lambda x:x==min(levels), levels))))
