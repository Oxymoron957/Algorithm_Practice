"""
2048
https://www.acmicpc.net/problem/12100
"""

from copy import deepcopy
from collections import deque

# input 
N = int(input())
map2048 = []
for i in range(N):
    map2048.append(list(map(int, input().split())))

# variables
max2048 = 0

def push2048(N, map2048, command):
    incomplete = False
    if command == 'UP':
        for i in range(N-1, 0, -1):
            for j, val in enumerate(map2048[i]):
                if map2048[i][j] != 0 and map2048[i-1][j] == 0:
                    incomplete = True
                    map2048[i][j] = 0
                    map2048[i-1][j] = val
        if incomplete:
            push2048(N, map2048, command)
    if command == 'DOWN':
        for i in range(0, N-1):
            for j, val in enumerate(map2048[i]):
                if map2048[i][j] != 0 and map2048[i+1][j] == 0:
                    incomplete = True
                    map2048[i][j] = 0
                    map2048[i+1][j] = val
        if incomplete:
            push2048(N, map2048, command)

    if command == 'RIGHT':
        for i, ival in enumerate(map2048):
            for j in range(0, N-1):
                if map2048[i][j] != 0 and map2048[i][j+1] == 0:
                    incomplete = True
                    map2048[i][j+1] = map2048[i][j]        
                    map2048[i][j] = 0
        if incomplete:
            push2048(N, map2048, command)

    if command == 'LEFT':
        for i, ival in enumerate(map2048):
            for j in range(N-1, 0, -1):
                if map2048[i][j] != 0 and map2048[i][j-1] == 0:
                    incomplete = True
                    map2048[i][j-1] = map2048[i][j]        
                    map2048[i][j] = 0
        if incomplete:
            push2048(N, map2048, command)

def sum2048(N, map2048, command):
    if command == 'UP':
        for i in range(N-1, 0, -1):
            for j, val in enumerate(map2048[i]):
                if map2048[i][j] == map2048[i-1][j]:
                    map2048[i][j] = 0
                    map2048[i-1][j] = val * 2
    if command == 'DOWN':
        for i in range(0, N-1):
            for j, val in enumerate(map2048[i]):
                if map2048[i][j] == map2048[i+1][j]:
                    map2048[i][j] = 0
                    map2048[i+1][j] = val * 2

    if command == 'RIGHT':
        for i, ival in enumerate(map2048):
            for j in range(0, N-1):
                if map2048[i][j] == map2048[i][j+1]:
                    map2048[i][j+1] = map2048[i][j] * 2       
                    map2048[i][j] = 0

    if command == 'LEFT':
        for i, ival in enumerate(map2048):
            for j in range(N-1, 0, -1):
                if map2048[i][j] == map2048[i][j-1]:
                    map2048[i][j-1] = map2048[i][j] * 2        
                    map2048[i][j] = 0

def command2048(N, map2048, command):    
    push2048(N, map2048, command)
    sum2048(N, map2048, command)
    push2048(N, map2048, command)
    return map2048

def getMax(map2048):
    val = 0
    for i in map2048:
        val = max(val, max(i))
    return val


# # recursive function
# def recur(map2048, command, level):
#     global N
#     global max2048
#     move = ['UP', 'DOWN', 'LEFT', 'RIGHT']
#     if level > 4:
#         return
#     # print(level)

#     if command != '':
#         command2048(N, map2048, command)
#         max2048 = max(max2048, getMax(map2048))

#     for m in move:
#         recur(deepcopy(map2048), m, level+1)

# recur(map2048, '', 0)

dq = deque()
dq.append((deepcopy(map2048), 0))

while dq:
    curMap, curStep = dq.popleft()

    if curStep > 5:
        max2048 = max(max2048, getMax(curMap))
        continue
    for command in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
        newMap = command2048(N, deepcopy(curMap), command)
        dq.append((deepcopy(newMap), curStep+1))

print(max2048)

