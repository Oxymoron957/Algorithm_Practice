# -*- coding: utf-8 -*-
"""
우유 축제
https://www.acmicpc.net/problem/14720
"""

N = (int)(input())
arr = list(map(int, input().split()))
cur = 0
answer = 0

# print(N, arr)
for milk in arr:
	if cur == milk:
		cur = (cur + 1) % 3
		answer += 1

print(answer)
