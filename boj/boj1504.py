"""
특정한 최단 경로
https://www.acmicpc.net/problem/1504
"""

from collections import deque
from copy import deepcopy

# input & init
N, E = list(map(int, input().split()))
graph = dict()
for i in range(E):
    p1, p2, w = list(map(int, input().split()))

    if graph.get(p1) == None:
        graph[p1] = [[p2, w]]
    else:
        graph[p1].append([p2, w])
    if graph.get(p2) == None:
        graph[p2] = [[p1, w]]
    else:
        graph[p2].append([p1, w])
checkPoints = list(map(int, input().split()))

weights = [float('inf')] * (N+1)
weights[0] = 0
weights[1] = 0

dq = deque()
dq.append([1, {1}])
flag = False
while dq:
    curPoint, curSet = dq.pop()
    nextSet = deepcopy(curSet)

    if graph.get(curPoint) == None:
        continue
    
    for nextPoint, w in graph[curPoint]:
        if weights[nextPoint] > weights[curPoint] + w:
            nextSet.add(nextPoint)
            if checkPoints[0] in list(curSet) and checkPoints[1] in list(curSet) and nextPoint == N:
                flag = True
                print(curSet)
                print(weights[nextPoint])
            weights[nextPoint] = weights[curPoint] + w
            
            dq.append([nextPoint, nextSet])

print(weights)