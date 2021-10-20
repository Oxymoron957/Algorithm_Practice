"""
마법사 상어와 파이어스톰
https://www.acmicpc.net/problem/20058

# 부족했던 점 : 
# 회전을 구현할 때 tmp 배열을 사용해서 간단히 해결할 수 있었다.
# dfs를 스택보단 재귀를 사용해서 간결하게 해결할 수 있었다. (visited 정보를 사용하지 않아도 됐다.)
"""

from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, Q = map(int, input().split())
N = 2 ** N
gameMap = [list(map(int, input().split())) for _ in range(N)]

for L in list(map(int, input().split())):
    # 증가량 계산
    increase_amount = 2 ** L
    # 회전 실시
    for x in range(0, N, increase_amount):
        for y in range(0, N, increase_amount):
            # 해당 구획의 내용을 tmp에 저장
            tmp = [gameMap[i][y:y + increase_amount] for i in range(x, x + increase_amount)]
            # tmp의 내용을 다시 game map에 복사한다.
            for col in range(increase_amount):
                for row in range(increase_amount):
                    gameMap[x + row][y + increase_amount - 1 - col] = tmp[col][row]

    # 인접한 얼음을 세기 위한 count map 초기화
    countMap = [[0] * N for _ in range(N)]
    # 인접한 얼음 계산 
    for x in range(0, N):
        for y in range(0, N):
            for delta in directions:
                newX, newY = x + delta[0], y + delta[1]
                if 0 <= newX < N and 0 <= newY < N and gameMap[newX][newY]:
                    countMap[x][y] += 1
    # 얼음 제거
    for x in range(0, N):
        for y in range(0, N):
            if gameMap[x][y] > 0 and countMap[x][y] < 3:
                gameMap[x][y] -= 1

# 남아있는 얼음의 합
print(sum(sum(i) for i in gameMap))

# (x,y)가 속한 덩어리의 크기
def dfs(x, y):
    ret = 1
    gameMap[x][y] = 0
    for delta in directions:
        nx, ny = x + delta[0], y + delta[1]
        if 0 <= nx < N and 0 <= ny < N and gameMap[nx][ny]:
            ret += dfs(nx, ny)
    return ret

# 제일 큰 덩어리
answer = 0
for x in range(N):
    for y in range(N):
        if gameMap[x][y] > 0:
            answer = max(answer, dfs(x, y))
            
print(answer)