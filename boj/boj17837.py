"""
새로운 게임2
https://www.acmicpc.net/problem/17837
"""

deltas = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]

def is_field(r, c): # 현재 row, col이 map 안에 있는지 확인
    return 0 <= r < N and 0 <= c < N

N, K = map(int, input().split())
map_color = [list(map(int, input().split())) for _ in range(N)]
map_piece = [[[] for _ in range(N)] for _ in range(N)] 
pieces = [] 
playtime = 0

for p in range(K): # piece의 정보를 pieces와 map_piece에 기록한다.
    r, c, direction = map(int, input().split())
    pieces.append([r-1, c-1, direction])
    map_piece[r-1][c-1].append(p)

while True:"""
퇴사
https://www.acmicpc.net/problem/14501
"""

N = int(input())

dp = [0] * (N+1)
T = []
P = []

for _ in range(N):
    input_ = list(map(int, input().split()))
    T.append(input_[0])
    P.append(input_[1])

# print(T, P)

# 거꾸로 생각하자 
for day in range(N-1, -1, -1):
    # 만약 day+T[day] > N 이라면 그 다음날과 cost가 같도록
    # print(N, day, T[day], P[day])
    if day + T[day] > N:
        dp[day] = dp[day+1]
    # day에 상담을 하지 않고 다음날로 넘어갈 경우, day에 상담을 해서 Pay를 받고 점프를 할 경우 비교 
    else: 
        dp[day] = max(dp[day+1], dp[day+T[day]]+P[day]) 

print(dp[0])
    toggle = False
    for p in range(K):
        now_r, now_c, now_direction = pieces[p] # 현재 위치정보
        delta_r, delta_c = deltas[now_direction] 
        next_r, next_c = now_r + delta_r, now_c + delta_c # 다음 위치정보
        next_direction = now_direction
        now_height = map_piece[now_r][now_c].index(p)

        move_pieces = map_piece[now_r][now_c][now_height:]

        map_piece[now_r][now_c] = map_piece[now_r][now_c][:now_height]

        if not is_field(next_r, next_c) or map_color[next_r][next_c] == 2: # 파란색 타일일 때
            if next_direction == 1:
                next_direction = 2
            elif next_direction == 2:
                next_direction = 1
            elif next_direction == 3:
                next_direction = 4
            elif next_direction == 4:
                next_direction = 3

            delta_r, delta_c = deltas[next_direction]
            pieces[p][2] = next_direction
            next_r, next_c = now_r + delta_r, now_c + delta_c

            if not is_field(next_r, next_c) or map_color[next_r][next_c] == 2: # 다음 타일도 파랑색이거나 바깥일 때 (움직이지 않는다.)
                next_r, next_c = now_r, now_c

            elif map_color[next_r][next_c] == 1: # 다음 타일이 빨간색일 때 (뒤집는다)
                move_pieces.reverse()

        elif map_color[next_r][next_c] == 1: # 빨간색 타일일때 (뒤집는다)
            move_pieces.reverse()

        for move_piece in move_pieces:
            pieces[move_piece][0], pieces[move_piece][1] = next_r, next_c # 움직이는 모든 piece의 위치정보 갱신

        map_piece[next_r][next_c] += move_pieces # 해당 위치에 더한다. 

        if len(map_piece[next_r][next_c]) >= 4: # 탈출 조건 
            toggle = True
            break

    playtime += 1

    if toggle:
        break

    if playtime > 1000:
        playtime = -1
        break

print(playtime)