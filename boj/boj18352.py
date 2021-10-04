"""
특정 거리의 도시 찾기
https://www.acmicpc.net/problem/18352
"""

from collections import deque

N, M, K, X = list(map(int, input().split()))

map_ = dict()
distance = dict()
for city in range(N):
    cityNum = city + 1
    distance[cityNum] = float('inf')
distance[X] = 0
for i in range(M):
    start, end = list(map(int, input().split()))
    if map_.get(start) == None:
        map_[start] = [end]
    else:
        (map_.get(start)).append(end)

dq = deque()
dq.append(X)
while dq:
    cur = dq.popleft()
    # print(cur)
    
    if map_.get(cur) == None:
        # print("check None")
        continue

    for next in map_[cur]:
        # print(next, distance[next], distance[cur] + 1)
        if distance[next] > distance[cur] + 1:
            distance[next] = distance[cur] + 1
            dq.append(next)

len_K = [x for x in distance.keys() if distance[x] == K]
if len_K:
    for i in len_K:
        print(i)
else:
    print(-1)