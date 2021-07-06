"""
미로 탐색
https://www.acmicpc.net/problem/2178
"""

N, M = map(int, input().split(' ')) # Row, Width

maze = []

for r in range(N):
    maze.append(input())

have_to_visit = [[0,0]] # 처음 시작지점은 0,0으로 설정한다. 
count = [[0] * M for _ in range(N)]
count[0][0] = 1 # 처음 시작부터 한칸을 차지하므로 1로 초기화한다.

while have_to_visit:
    cur_pos = have_to_visit.pop(0) # 다음 위치를 가져온다.
    
    if cur_pos[0] == N-1 and cur_pos[1] == M-1: # 만약 종착지일 경우 이동량을 출력하고 종료한다. 
        print(count[N-1][M-1])
        break

    for d in [[-1,0], [1,0], [0,-1], [0,1]]:
        next_y = d[0] + cur_pos[0] # 상하좌우 이동 위치를 계산한다.
        next_x = d[1] + cur_pos[1]

        if 0 <= next_y <= N-1 and 0 <= next_x <= M-1 and count[next_y][next_x] == 0: # 움직인 다음 좌표가 지도 내라면 + 지나간 적 없다면 
            if maze[next_y][next_x] == '1': # 다음에 지나갈 좌표가 1이라면 
                have_to_visit.append([next_y, next_x]) # 다음에 방문해야할 좌표로 추가
                count[next_y][next_x] = count[cur_pos[0]][cur_pos[1]] + 1 # 이전 위치의 이동량에서 1 추가 

        
"""
1 : 갈 수 있는 곳
0 : 갈 수 없는 곳
시작 : (0,0)
갈 수 있는 방향 : 언제나 4방향

4개의 자식을 가진 class : 각자 현제 인덱스를 가지고 있다. 

final_level = []
visited = []
class RAT:
    def __init__(self, pos_x, pos_y, level):
        global M, N, visited, final_level
        
        visited.append([pos_x, pos_y])
        
        if pos_x == M - 1  and pos_y == N - 1:
            final_level.append(level)
        print(level, [pos_x, pos_y])
        if 1 <= pos_x and maze[pos_y][pos_x-1] == '1' and not [pos_x-1, pos_y] in visited: # 왼쪽
            RAT(pos_x-1, pos_y, level+1)
        if pos_x <= M-2 and maze[pos_y][pos_x+1] == '1' and not [pos_x+1, pos_y] in visited: # 오른쪽           
            RAT(pos_x+1, pos_y, level+1)
        if 1 <= pos_y  and maze[pos_y -1][pos_x] == '1' and not [pos_x, pos_y-1] in visited: # 위     
            RAT(pos_x, pos_y-1, level+1)
        if pos_y <= N-2 and maze[pos_y +1][pos_x] == '1' and not [pos_x, pos_y+1] in visited: # 아래
            RAT(pos_x, pos_y+1, level+1)
            
"""


        
