"""
숫자의 표현
https://programmers.co.kr/learn/courses/30/lessons/12924
"""

from collections import deque

def solution(n):
    dq = deque()
    answer = 0
    cur = 1
    sum_ = 0
    while cur != n+1:
        if sum_ < n:
            sum_ += cur
            dq.append(cur)
            cur += 1
        if sum_ > n:
            sum_ -= dq.popleft()
        if sum_ == n:
            print(dq)
            sum_ -= dq.popleft()
            answer += 1
    return answer


print(solution(15))