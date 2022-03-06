# -*- coding: utf-8 -*-
"""
위장
https://programmers.co.kr/learn/courses/30/lessons/42578
"""

from itertools import combinations

def get_multi(li):
    answer = 1
    if not li:
        return 0
    for i in li:
        answer *= i
    return answer

def solution(clothes):
    hash_map = {}
    answer = 1
    for _, category_ in clothes:
        if hash_map.get(category_) == None:
            hash_map[category_] = 1
        else:
            hash_map[category_] += 1
    # for i in range(1, len(hash_map.keys())+1):
    #     answer += sum(map(get_multi, combinations(hash_map.values(), i)))
    for i in hash_map.values():
        answer *= i+1
    return answer-1

print(solution([["yellowhat", "headgear"], [ "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"], ["C", "pants"], ["D", "tops"], ["E", "tops"]]))
# print(solution([[]]))
