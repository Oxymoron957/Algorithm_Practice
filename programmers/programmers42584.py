# -*- coding: utf-8 -*-
"""
주식가격
https://programmers.co.kr/learn/courses/30/lessons/42584
"""

def solution(prices):
    answer = []
    for i in range(len(prices)):
        rise_time = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                rise_time += 1
            else:
                rise_time += 1
                break
        answer.append(rise_time)
    return answer

print(solution([1, 2, 0, 2, 3]))