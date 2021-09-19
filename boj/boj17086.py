"""
아기 상어 2
https://www.acmicpc.net/problem/17086
"""

from copy import deepcopy
from collections import deque

dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]

# input 
N, M = list(map(int, input().split()))
map_data = []
map_data_search = []
shark_loc = []
for row in range(N):
    col = list(map(int, input().split()))
    map_data.append(col)
    map_data_search.append(deepcopy(col))
    while 1 in col:
        shark_loc.append([row, col.index(1)])
        col[col.index(1)] = -1

# print(shark_loc)
# print(map_data)
# print(map_data_search)

# run bfs from the shark locations 
for loc in shark_loc:
    dq = deque()
    dq.append([loc[0], loc[1]])
    while dq:
        curx, cury = dq.popleft()
        
        for i in range(8):
            nx = curx + dx[i]
            ny = cury + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # print(nx, ny)
                # print(map_data_search[nx])
                if map_data_search[nx][ny] > map_data_search[curx][cury] + 1 or map_data_search[nx][ny]==0:
                    dq.append([nx, ny])
                    map_data_search[nx][ny] = map_data_search[curx][cury] + 1
# print(map_data_search) 

maxVal = 0
for i in map_data_search:
    maxVal = max(maxVal, max(i))
print(maxVal-1)
# print()