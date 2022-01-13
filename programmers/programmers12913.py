"""
땅따먹기
https://programmers.co.kr/learn/courses/30/lessons/12913
"""

def solution(land):
    for row_index in range(1, len(land)):
        for i in range(4):
            exclude_list = land[row_index-1][:i] + land[row_index-1][i+1:]
            land[row_index][i] += max(exclude_list)
    return max(land[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
