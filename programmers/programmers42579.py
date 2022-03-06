# -*- coding: utf-8 -*-
"""
2022 03 06
베스트엘범
https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3
"""

def solution(genres, plays):
	hash_map = {}
	orders = []
	for i in range(len(genres)):
		if hash_map.get(genres[i]) == None:
			hash_map[genres[i]] = [[plays[i], i]]
		else:
			hash_map[genres[i]].append([plays[i], i])
	# print(hash_map)

	orders = []
	for key in hash_map.keys():
		hash_map[key] = sorted(hash_map[key], key= lambda x:x[1])
		hash_map[key] = sorted(hash_map[key], key= lambda x:x[0], reverse= True)
		orders.append([key, sum(map(lambda x:x[0], hash_map[key]))])
	orders.sort(key=lambda x:x[1], reverse=True)
	print(hash_map)
	print(orders)
	
	answer = []
	for key, _ in orders:
		if len(hash_map[key]) == 1:
			answer.append(hash_map[key][0][1])
		else:
			answer.append(hash_map[key][0][1])
			answer.append(hash_map[key][1][1])
	return answer

	

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 500, 500, 2500]))