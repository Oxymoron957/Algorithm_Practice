"""
치즈
https://www.acmicpc.net/problem/2638
"""

from collections import deque
from copy import deepcopy

N, M = list(map(int, input().split()))
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

answer = 0
while True:
    st = deque()
    checked = [[ 0 for _ in range(M)] for _ in range(N)]
    outside = [[ 0 for _ in range(M)] for _ in range(N)]
    # inspect every corner
    for r in range(N):
        for c in range(M):
            if r == 0 or r == N-1:
                st.append([r, c])
                checked[r][c] = 1
            elif c == 0 or c == M-1:
                st.append([r, c]) 
                checked[r][c] = 1

    while st:
        cur_r, cur_c = st.pop()

        for d_r, d_c in [[1,0], [-1,0], [0,1], [0,-1]]:
            next_r, next_c = cur_r+d_r, cur_c+d_c
            if 0 <= next_r < N and 0 <= next_c < M:
                # print(next_r, next_c)
                if checked[next_r][next_c] != 1:
                    st.append([next_r, next_c])
                    checked[next_r][next_c] = 1
                    outside[next_r][next_c] += 1
    
    for r in range(N):
        for c in range(M):
            if maps[r][c] == 1 and outside[r][c] >= 2:
                maps[r][c] = 0
                answer += 1
    for i in outside:
        print(i)
    
    break

# print(maps)
# for i in maps:
#     print(i)