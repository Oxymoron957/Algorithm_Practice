"""
알파벳
https://www.acmicpc.net/problem/1987
"""

from collections import deque
import sys

R, C = list(map(int, sys.stdin.readline().split()))

maps = []
for i in range(R):
    maps.append(list(sys.stdin.readline()))

dq = deque()
dq.append([0,0, set(maps[0][0])])

answer = 0
while dq:
    curx, cury, passed = dq.pop()

    for dx, dy in [[1,0], [0,1], [-1,0], [0,-1]]:
        nx, ny = curx+dx, cury+dy
        if 0 <= nx < C and 0 <= ny < R:
            if maps[ny][nx] not in passed:
                passed_ = set(passed)
                passed_.add(maps[ny][nx])
                answer = len(passed_) if answer < len(passed_) else answer
                dq.append([nx, ny, passed_])
print(answer)


