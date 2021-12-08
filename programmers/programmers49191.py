"""
순위
https://programmers.co.kr/learn/courses/30/lessons/49191
"""

def solution(n, results):
    fighters = dict()
    for i in range(1, n+1):
        # print(i)
        fighters[i] = [[], []]
    for win, lose in results:
        fighters[win][0].append(lose)
        fighters[lose][1].append(win)
    
    answer = 0
    for win, lose in fighters.values():
        # print(win, lose)
        if len(win) + len(lose) == n-1:
            answer+=1
            if len(win) == 1:
                answer += 1
            if len(lose) == 1:
                answer += 1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))