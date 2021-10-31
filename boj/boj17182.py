"""
우주 탐사선
https://www.acmicpc.net/problem/17182
"""

from collections import deque
from copy import deepcopy

N, K = list(map(int, input().split()))

stars = []

for i in range(N):
    stars.append(list(map(int, input().split())))

# print(N, K)
# print(stars)

stack = deque()

stack.append([0, K, 0, [K]])
answers = []
while stack:
    iter, curLoc, curCost, curVisit = stack.pop()
    nextDest = stars[curLoc]

    if len(curVisit) == N:
        answers.append(curCost)
        continue

    if iter > N:
        continue

    for i, cost in enumerate(nextDest):
        if i != curLoc:
            # nextVisit = deepcopy(curVisit)
            # curVisit.add(i)
            stack.append([iter+1, i, curCost+cost, list(set(curVisit+[i]))])

print(min(answers))
