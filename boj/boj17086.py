"""
아기 상어 2
https://www.acmicpc.net/problem/17086
"""

from copy import deepcopy

def get_distance(loc1, loc2):
    loc1 = deepcopy(loc1)
    loc2 = deepcopy(loc2)
    dist = 0
    while loc1 != loc2:

        if loc1[0] == loc2[0] and loc1[1] > loc2[1]:
            dist += 1
            loc2[1] += 1
        if loc1[0] == loc2[0] and loc1[1] < loc2[1]:
            dist += 1
            loc1[1] += 1
        if loc1[0] > loc2[0] and loc1[1] == loc2[1]:
            dist += 1
            loc2[0] += 1
        if loc1[0] < loc2[0] and loc1[1] == loc2[1]:
            dist += 1
            loc1[0] += 1

        if loc1[0] > loc2[0] and loc1[1] > loc2[1]:
            dist += 1
            loc2[0] += 1
            loc2[1] += 1
        if loc1[0] < loc2[0] and loc1[1] < loc2[1]:
            dist += 1
            loc1[0] += 1
            loc1[1] += 1
        if loc1[0] > loc2[0] and loc1[1] < loc2[1]:
            dist += 1
            loc2[0] += 1
            loc1[1] += 1
        if loc1[0] < loc2[0] and loc1[1] > loc2[1]:
            dist += 1
            loc1[0] += 1
            loc2[1] += 1
    return dist
                


# input 
N, M = list(map(int, input().split()))
map_data = []
shark_loc = []
for row in range(N):
    col = list(map(int, input().split()))
    map_data.append(col)
    while 1 in col:
        shark_loc.append([row, col.index(1)])
        col[col.index(1)] = -1

# print(map_data)
# print(shark_loc)

# calculate distances
answer = -1
for i, loc1 in enumerate(shark_loc):
    for j, loc2 in enumerate(shark_loc[i+1:]):
        # print(loc1, loc2)
        # print(shark_loc[i+1:])
        # print(get_distance(loc1, loc2))
        answer = get_distance(loc1, loc2) if answer == -1 else max(answer, get_distance(loc1, loc2))

print(answer)