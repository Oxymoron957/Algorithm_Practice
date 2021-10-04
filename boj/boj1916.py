"""
최소비용 구하기
https://www.acmicpc.net/problem/1916
"""

from collections import deque
from queue import PriorityQueue

N = int(input())
M = int(input())

buses = dict()
for i in range(M):
    start, end, weight = list(map(int, input().split()))
    if buses.get(start) == None:
        buses[start] = [[end, weight]]
    else:
        buses[start].append([end, weight])

start, end = list(map(int, input().split()))

weights = dict()
for i in range(N):
    weights[i+1] = float('inf')
weights[start] = 0

# dq = deque()
# dq.append(start)
dq = PriorityQueue()
dq.put(buses[start][0])

while dq:
    print(dq)
    curLocation, curWeight = dq.get()

    if buses.get(curLocation) == None:
        continue

    for nextLocation, weight in buses[curLocation]:
        if weights[nextLocation] > weights[curLocation] + weight:
            weights[nextLocation] = weights[curLocation] + weight
            dq.put(nextLocation)

print(weights)
print(weights[end])
