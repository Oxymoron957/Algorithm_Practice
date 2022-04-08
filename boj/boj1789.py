# -*- coding: utf-8 -*-
"""
수들의 합
https://www.acmicpc.net/problem/1789
"""

S = int(input())

idx = 1
while (idx * (idx + 1) / 2) + idx < S:
	idx += 1

print(idx)
