# -*- coding: utf-8 -*-
"""
순위
https://programmers.co.kr/learn/courses/30/lessons/49191
"""

from collections import deque


def solution(n, results):
    result = {}
    for win, lose in results:
        if result.get(win) == None:
            result[win] = [[lose], []]
        else:
            result[win][0].append(lose)
        if result.get(lose) == None:
            result[lose] = [[], [win]]
        else:
            result[lose][1].append(win)
    print(result)
    for i in range(1, n+1):
        print(i)
        visited = set()
        dq = deque()
        dq.append(i)
        while dq:
            cur_node = dq.popleft()
            print(cur_node)
            for next_node in result.get:
                visited.add(next_node)
                dq.append(next_node)
        print(i, visited)
                
    # print(result)
    # answer = 0
    # for i in result.keys():
    #     if len(result[i][0]) + len(result[i][1]) == n-1:
    #         answer += 1
    #         if len(result[i][0]) == 1 or len(result[i][1]) == 1:
    #             answer += 1
    
    # return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))