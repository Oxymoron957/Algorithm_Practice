"""
숨바꼭질
https://www.acmicpc.net/problem/1697

몰랐던 점 :
그래프 탐색 문제에서 탈출조건을 잘 생각하자
"""

import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))

MAX = 10**5
q = deque()
cost = [0] * (MAX+1) # 각 위치까지 오는 최단 cost를 저장하는 리스트

q.append(N)

while q:
    cur_x = q.popleft()

    if cur_x == K:
        print(cost[cur_x])
        break

    for new_x in (cur_x-1, cur_x+1, cur_x*2):
        if 0 <= new_x <= MAX and not cost[new_x]: # 이미 계산되지 않은 x위치에서만 계산하도록 
            cost[new_x] = cost[cur_x] + 1
            q.append(new_x)


