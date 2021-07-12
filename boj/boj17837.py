"""
새로운 게임 2
https://www.acmicpc.net/problem/17837
"""


        

# N, K 입력받기 
N, K = list(map(int, input().split()))

# init Map (index order : col, row)
gameMap = [[0]*N for _ in range(N)]
gameMap_piece = [[]*N for _ in range(N)]

# init Tile
for height in range(N):
    row = list(map(int, input().split(' ')))
    for i in range(N):
        gameMap[height][i] = row[i]

# for i in gameMap:
#     print(i)
# print()

# init chess piece class
class Chesspiece:
    def __init__(self, y, x, dir):
        self.cur_y = y
        self.cur_x = x
        self.direction = dir
    


# init chess piece info 
pieces = []
for p in range(K):
    pieceInfo = list(map(int, input().split(' ')))
    pieces.append(Chesspiece(pieceInfo[1], pieceInfo[0], pieceInfo[2]))

turn = 0
isNotDone = True
while isNotDone:
    for p in pieces:
        next_coord_x, next_coord_y = 0, 0
        # check direction
        if p.direction == 1:
            next_coord_y, next_coord_x = [p.cur_y, p.cur_x+1]
        elif p.direction == 2:
            next_coord_y, next_coord_x = [p.cur_y, p.cur_x-1]
        elif p.direction == 3:
            next_coord_y, next_coord_x = [p.cur_y+1, p.cur_x]
        elif p.direction == 4:
            next_coord_y, next_coord_x = [p.cur_y-1, p.cur_x]
        # check next tile
        if not (0<= next_coord_x <=N and 0<= next_coord_x <=N):
            pass
        next_tile = gameMap[next_coord_y, next_coord_x]

        if next_tile == 1:
            p.cur_y, p.cur_x = next_coord_y, next_coord_x
            

    for row in gameMap_piece:
        for pList in row:
            if len(pList) >= 4:
                isNotDone = False

print(turn)

