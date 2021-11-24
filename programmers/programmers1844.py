"""
게임 맵 최단거리
https://programmers.co.kr/learn/courses/30/lessons/1844

몰랐던 점 : cost를 하나의 값으로 저장하지 말고 visited와 함께 쓰면 시간적 효율 ++
"""

from collections import deque

def solution(maps):
    n = len(maps) # rows
    m = len(maps[0]) # cols

    visited = [[-1 for x in range(m)] for y in range(n)]  # not visited -1
    visited[0][0] = 1
    queue_ = deque()
    queue_.append([0,0])

    while queue_:
        cur_row, cur_col = queue_.popleft()

        # 원래는 cost도 같이 계산하고 queue에 저장하는 방식 -> 시간 많이 듦!
        # if cur_row == n-1 and cur_col == m-1:
        #     return cur_cost
        
        for d_row, d_col in [[1,0], [-1,0],[0,1],[0,-1]]:
            next_row = cur_row+d_row
            next_col = cur_col+d_col
            if (0 <= next_row < n and 0 <= next_col < m):
                if visited[next_row][next_col] == -1:
                    if maps[next_row][next_col] == 1:
                        visited[next_row][next_col] = visited[cur_row][cur_col]+1
                        queue_.append([next_row, next_col])

    return visited[n-1][m-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
