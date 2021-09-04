"""
최단경로
https://www.acmicpc.net/problem/1753
"""

from collections import deque
import sys

# input
V, E = list(map(int, sys.stdin.readline().split()))
startVertex = int(sys.stdin.readline())

# variables
vertex = {}
weight = {}

# init graph & weight
for n in range(1, V+1):
    weight[n] = float('inf')
weight[startVertex] = 0
for i in range(E):
    v1, v2, w = list(map(int, input().split()))
    vertex[v1] = vertex.get(v1, []) + [(v2, w)]

# traverse
q = deque()
q.append(startVertex)
while q:
    curVertex = q.popleft()
    if vertex.get(curVertex) == None:
        continue
    for nextVertex, w in vertex[curVertex]:
        if weight[nextVertex] > weight[curVertex] + w:
            weight[nextVertex] = weight[curVertex] + w
            q.append(nextVertex)

# print
for i in [x if x != float('inf') else 'INF' for x in weight.values()]:
    print(i)
