"""
짝 지어 제거하기
https://programmers.co.kr/learn/courses/30/lessons/12973

* 부족했던 점 : 
문제를 너무 단순하게 보고 Stack 문제인 것을 캐치하지 못했다..  
"""

from collections import deque

def solution(s):
    dq = deque()

    for c in s:
        if not dq:
            dq.append(c)
        else:
            if dq[-1] == c:
                dq.pop()
            else:
                dq.append(c)

    if dq:
        return 0
    else:
        return 1

# def solution(s):
#     sList = list(s)
#     sIdx = 0
#     while sIdx + 1 < len(sList): 
#         if sList[sIdx] == sList[sIdx+1]:
#             sList.pop(sIdx)
#             sList.pop(sIdx)
#             sIdx -= 1 if sIdx != 0 else sIdx
#         else:
#             sIdx += 1
    
#     return 1 if not sList else 0

print(solution('baaaa'))
print(solution('baabaa'))
print(solution('cdcd'))
