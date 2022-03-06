# -*- coding: utf-8 -*-
"""
완주하지 못한 선수
https://programmers.co.kr/learn/courses/30/lessons/42576
"""

def solution(participant, completion):
	sort_p = sorted(participant)
	sort_c = sorted(completion)
	for i in range(len(completion)):
		if (sort_p[i] != sort_c[i]):
			return sort_p[i]
	return sort_p[-1]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution( ["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
