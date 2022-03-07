# -*- coding: utf-8 -*-
"""
더 맵게
https://programmers.co.kr/learn/courses/30/lessons/42626
"""

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) >= 2 and scoville[0] <= K:
        least_spicy = heapq.heappop(scoville)
        second_spicy = heapq.heappop(scoville)
        heapq.heappush(scoville, least_spicy+second_spicy*2)
        answer += 1
    if scoville[0] < K:
        return -1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([0, 1], 10))