"""
벽 부수고 이동하기
https://www.acmicpc.net/problem/2206
"""

from collections import deque

# input 
N, M = list(map(int, input().split()))
originalMap = []
for i in range(N):
    originalMap.append(list(map(int, list(input()))))

# print(N, M)
# print(originalMap)

# make visitedInfo
visitedMap = [[[0]*2 for _ in range(M)] for __ in range(N)]
# print(visitedMap)

# init bfs
q = deque()
q.append([0, 0, 1])
visitedMap[0][0][1] = 1

while q:
    # 이번에 이동할 node pop
    x, y, canBreak = q.popleft()
    # 목적지에 도착할 경우 print & break
    if x == N-1 and y == M-1:
        print(visitedMap[x][y][canBreak])
        break
    # 이동할 방향 결정
    for moveX, moveY in [[1,0], [-1, 0], [0, 1], [0, -1]]:
        # 이동한 x,y 계산
        nx = x + moveX
        ny = y + moveY
        # 아직 지도 안에 있을 경우만 
        if 0 <= nx < N and 0 <= ny < M:
            # 벽이 있고 부술 수 있을 경우
            if originalMap[nx][ny] == 1 and canBreak == 1:
                visitedMap[nx][ny][0] = visitedMap[x][y][1] + 1
                q.append([nx, ny, 0])
            # 벽이 없고 부술 수 없을 경우
            elif originalMap[nx][ny] == 0 and visitedMap[nx][ny][canBreak] == 0:
                visitedMap[nx][ny][canBreak] = visitedMap[x][y][canBreak] + 1
                q.append([nx, ny, 0])

