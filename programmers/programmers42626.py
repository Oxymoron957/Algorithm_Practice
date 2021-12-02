"""
더 맵게
https://programmers.co.kr/learn/courses/30/lessons/42626

탈출 조건에 유의하자!
"""

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        newScov = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, newScov)
        answer += 1

        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))