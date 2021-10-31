"""
봄버맨
https://www.acmicpc.net/problem/16918
"""

from copy import deepcopy

# input
R, C, N = list(map(int, input().split()))

# variables
gameMap = []
bombLoc = []
all_bomb_map = []

for row in range(R):
    col = list(input())

    gameMap.append(col)
    all_bomb_map.append(['O']*C)

    for i in range(len(col)):
        if col[i] == 'O':
            bombLoc.append([row, i])

def activateBomb():
    global gameMap, bombLoc
    for row, col in bombLoc:
        if gameMap[row][col] == 'O':
            gameMap[row][col] = '.'
        if row -1 >= 0 and gameMap[row-1][col] == 'O':
            gameMap[row-1][col] = '.'
        if row +1 <= R-1 and gameMap[row+1][col] == 'O':
            gameMap[row+1][col] = '.'
        if col -1 >= 0 and gameMap[row][col-1] == 'O':
            gameMap[row][col-1] = '.'
        if col +1 <= C-1 and gameMap[row][col+1] == 'O':
            gameMap[row][col+1] = '.'

    bombLoc = []
    for row in range(R):
        for col in range(C):
            if gameMap[row][col] == 'O':
                bombLoc.append([row, col])

# bombLoc = deepcopy(bombLoc)
for second in range(1, N+1):
    if second == 1:
        # print('1 second -> do nothing')
        continue
    if second % 2 == 0:
        gameMap = deepcopy(all_bomb_map)
    else:
        activateBomb()

    # print(second)
    # for i in gameMap:
    #     print("".join(i))
    # print()


for i in gameMap:
    print("".join(i))
