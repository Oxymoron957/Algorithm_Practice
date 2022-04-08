# -*- coding: utf-8 -*-
"""
가장 먼 노드
https://programmers.co.kr/learn/courses/30/lessons/49189
"""

from collections import deque

def solution(n, edge):
	graph = {}
	for line in edge:
		if graph.get(line[0]) == None:
			graph[line[0]] = [line[1]]
		else:
			graph[line[0]].append(line[1])
		if graph.get(line[1]) == None:
			graph[line[1]] = [line[0]]
		else:
			graph[line[1]].append(line[0])
	# print(graph)

	cost = [float('inf')] * n
	cost[0] = 0
	
	queue = deque()
	queue.append(1)
	while queue:
		cur_node = queue.popleft()
		for next_node in graph[cur_node]:
			# print(next_node)
			if cost[next_node-1] > cost[cur_node-1] + 1:
				cost[next_node-1] = cost[cur_node-1] + 1
				queue.append(next_node)
	longest = max(cost)
	answer = 0
	for i in cost:
		if i == longest:
			answer += 1
	return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))