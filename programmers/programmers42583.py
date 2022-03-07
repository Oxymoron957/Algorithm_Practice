# -*- coding: utf-8 -*-
"""
다리를 지나는 트럭
https://programmers.co.kr/learn/courses/30/lessons/42583
"""

def solution(bridge_length, weight, truck_weights):
	bef_bridge = []
	on_bridge = []
	off_bridge = []
	cur_w = 0

	for e in truck_weights:
		bef_bridge.append([e, 0])
	
	answer = 1
	cnt = 5
	while len(off_bridge) != len(truck_weights) and cnt:
		# print(bef_bridge)
		# print(on_bridge)
		# print(off_bridge)
		# print("\n")		
		# 다리에 트럭 올리기
		if bef_bridge and cur_w+bef_bridge[0][0] <= weight:
			cur_w += bef_bridge[0][0]
			on_bridge.append(bef_bridge[0])
			bef_bridge.pop(0)
		
		# 다리에 있는 트럭 이동하기
		for i in range(len(on_bridge)):
			on_bridge[i][1] += 1
		
		# 완료한 트럭 옮기기 
		if on_bridge and on_bridge[0][1] >= bridge_length:
			cur_w -= on_bridge[0][0]
			off_bridge.append(on_bridge[0])
			on_bridge.pop(0)
		answer += 1
		# cnt -= 1
	return answer

	
	
print(solution(2, 10, [7,4,5,6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
