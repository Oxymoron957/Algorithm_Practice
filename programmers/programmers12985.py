"""
예상 대진표
https://programmers.co.kr/learn/courses/30/lessons/12985
"""

def solution(n,a,b):
    if abs(a-b) == 1:
        return 1
    answer = 0
    while a != b:
        a = int((a+1)/2)
        b = int((b+1)/2)
        answer += 1
    

    return answer


print(solution(8, 4, 7))