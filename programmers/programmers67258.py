"""
보석 쇼핑
https://programmers.co.kr/learn/courses/30/lessons/67258
"""

from collections import deque

def check(gem, dq):
    index_ = 0
    print(gem, dq)
    if dq[0] == gem:
        dq.popleft()
        index_ += 1
        while len(dq)>=2 and dq[0] == dq[1]:
            dq.popleft()
            index_ += 1
    return index_
            
def solution(gems):
    # gem의 종류를 파악한다. 
    gemSet = set(gems)

    # index 설정
    startIdx = 1
    endIdx = 1

    # 
    answer = []

    # Index 1부터 탐색 시작한다. 
    dq = deque()
    dq.append(gems[0])
    for g in gems[1:]:
        if set(dq) == gemSet:
            if not answer:
                answer = [startIdx, endIdx]
            elif answer[1] - answer[0] > endIdx - startIdx:
                answer = [startIdx, endIdx]

        startIdx += check(g, dq)
        dq.append(g)
        endIdx += 1 
        
        
    return answer
            

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
