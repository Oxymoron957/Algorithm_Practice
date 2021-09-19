"""
구명보트 
https://programmers.co.kr/learn/courses/30/lessons/42885
"""

from collections import deque

def solution(people, limit):
    # 정렬
    people.sort()
    # 덱 자료구조로 변경
    dq = deque(people)
    # 필요한 구명보드 수
    answer = 0
    while dq:
        # print(dq)
        # 대기 사람이 하나만 있으면 구명보트가 무조건 하나 더 필요
        if len(dq) == 1:
            answer += 1
            break
        # 가장 가벼운 사람과 가장 무거운 사람이 limit 이내면 가장 효율적으로 같이 탈수 있다.
        if dq[0] + dq[-1] <= limit:
            answer += 1
            dq.pop()
            dq.popleft()
        # 그렇지 않으면 가장 무거운 사람은 혼자 탈 수밖에 없다. 
        else:
            answer += 1
            dq.pop()
    return answer

print(solution([70,50, 80], 100))
print(solution([70,50,50,80], 100))
