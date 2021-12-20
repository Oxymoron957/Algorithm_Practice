"""
알파벳
https://www.acmicpc.net/problem/1987

몰랐던 점 : bfs에서 deque가 아니라 set 자료구조를 사용하는게 더 빠르다. 
"""

from collections import deque
import sys

R, C = list(map(int, sys.stdin.readline().split()))

maps = []
for i in range(R):
    maps.append(list(sys.stdin.readline()))

## 예전코드 
# dq = deque()
# dq.append([0,0, set(maps[0][0])])

# answer = 0
# while dq:
#     curx, cury, passed = dq.pop()

#     for dx, dy in [[1,0], [0,1], [-1,0], [0,-1]]:
#         nx, ny = curx+dx, cury+dy
#         if 0 <= nx < C and 0 <= ny < R:
#             if maps[ny][nx] not in passed:
#                 passed_ = set(passed)
#                 passed_.add(maps[ny][nx])
#                 answer = len(passed_) if answer < len(passed_) else answer
#                 dq.append([nx, ny, passed_])

answer = 1
q = set([(0,0, maps[0][0])])

while q:
    curx, cury, ans = q.pop()

    for dx, dy in [[1,0], [0,1], [-1,0], [0,-1]]:
        nx, ny = curx+dx, cury+dy

        if 0 <= nx < C and 0 <= ny < R:
            if maps[ny][nx] not in ans:
                q.add((nx, ny, ans + maps[ny][nx]))
                answer = max(answer, len(ans)+1)


print(answer)


