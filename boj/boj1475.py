# -*- coding: utf-8 -*-
"""
방 번호
https://www.acmicpc.net/problem/1475
"""

from math import ceil

N = input()

nums = dict()

for i in range(0, 10):
	nums[i] = 0

for i in N:
	if i == '9':
		nums[6]+=1
	else:
		nums[int(i)]+=1

if nums[6] == max(nums.values()) and len(list(filter(lambda x: x==max(nums.values()), nums.values()))) == 1:
	print(ceil(nums[6]/2))
else:
	print(max(nums.values()))