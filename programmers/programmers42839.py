# -*- coding: utf-8 -*-
"""
소수 찾기
https://programmers.co.kr/learn/courses/30/lessons/42839
"""

from itertools import permutations

def is_prime(num):
	if num < 2:
		return False
	if num == 2:
		return True
	last_num = num ** 0.5
	for i in range(2, int(last_num)+2):
		if num % (i) == 0:
			return False
	return True
	

def solution(numbers):
	li = list(numbers)
	answer = 0
	has_been = set()
	for i in range(1, len(li)+1):
		for num in set(permutations(li, i)):
			if is_prime(int("".join(num))) and int("".join(num)) not in has_been:
				answer += 1
				has_been.add(int("".join(num)))
	return answer

print(solution("17"))
print(solution("011"))
