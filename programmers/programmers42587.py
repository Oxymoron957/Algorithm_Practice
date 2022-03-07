# -*- coding: utf-8 -*-
"""
프린터
https://programmers.co.kr/learn/courses/30/lessons/42587
"""

def solution(priorities, location):
    stack = []
    for i, e in enumerate(priorities):
        if i == location:
            stack.append([e, True])
        else:
            stack.append([e, False])
    answer = 1
    while stack:
        if stack[0][0] >= max(stack, key= lambda x:x[0])[0]:
            if stack[0][1]:
                return answer
            else:
                stack.pop(0)
                answer += 1
        else:
            stack.append(stack[0])
            stack.pop(0)
        

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
