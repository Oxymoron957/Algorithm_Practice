# -*- coding: utf-8 -*-
"""
2022 03 06
기능개발
https://programmers.co.kr/learn/courses/30/lessons/42586
"""

def solution(progresses, speeds):
	answer = []

	while progresses:	
		works_done = 0
		for i in range(len(progresses)):
			progresses[i] += speeds[i]
		
		while progresses and progresses[0] >= 100:
			works_done += 1
			progresses.pop(0)
			speeds.pop(0)
		
		if works_done != 0:
			answer.append(works_done)
	return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# li = [1,2,3]
# li.pop()