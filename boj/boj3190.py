"""
뱀
https://www.acmicpc.net/problem/3190
"""

N = int(input())
apples = int(input())
maps = [[0]*N for _ in range(N)]

for _ in range(apples):
    row, col = map(int, input().split())
    maps[row-1][col-1] = 1

for _ in maps:
    print(_)

L = int(input())
scenario = []
for _ in range(L):
    t, d = input().split()
    t = int(t)
    scenario.append([t, d])

print(scenario)

time = 0
move_log = [[0,0]]
snake_len = 1
cur_loc = [0, 0]
cur_dir = [0, 1]

test = 22
while test:
    test -= 1

    print(cur_loc, cur_dir, scenario)
    time += 1
    cur_loc[0] += cur_dir[0]
    cur_loc[1] += cur_dir[1]
    move_log.append([cur_loc[0], cur_loc[1]])
    print(time, cur_loc, move_log[1:snake_len])
    if cur_loc in move_log[1:snake_len]:
        print("Lost\n")
        break
    if not (0 <= cur_loc[0] < N):
        print("mapout")
        break
    if not (0 <= cur_loc[1] < N):
        print("mapout")
        break
    if scenario and scenario[0][0] == time:
        if cur_dir[0] == -1 and cur_dir[1] == 0 and scenario[0][1] == 'L':
            cur_dir = [0, -1]
        elif cur_dir[0] == -1 and cur_dir[1] == 0 and scenario[0][1] == 'D':
            print("-10")
            cur_dir = [0, 1]

        elif cur_dir[0] == 1 and cur_dir[1] == 0 and scenario[0][1] == 'L':
            cur_dir = [0, 1]
        elif cur_dir[0] == 1 and cur_dir[1] == 0 and scenario[0][1] == 'D':
            print("10")
            cur_dir = [0, -1]
        
        elif cur_dir[0] == 0 and cur_dir[1] == -1 and scenario[0][1] == 'L':
            cur_dir = [1, 0]
        elif cur_dir[0] == 0 and cur_dir[1] == -1 and scenario[0][1] == 'D':
            print("0-1")
            cur_dir = [-1, 0]
        
        elif cur_dir[0] == 0 and cur_dir[1] == 1 and scenario[0][1] == 'L':
            cur_dir = [-1, 0]
        elif cur_dir[0] == 0 and cur_dir[1] == 1 and scenario[0][1] == 'D':
            print("01")
            cur_dir = [1, 0]
        snake_len += 1
        scenario.pop(0)
    # if not scenario:
    #     print("complete\n")
    #     break
print(time)





























"""
N = int(input())
K = int(input())

# Map Generation 
map = [['0']*N for _ in range(N)]

for i in range(K):
    x, y = [int(x) for x in input().split(' ')]
    map[x-1][y-1] = '1'

T = int(input())
queue = []
for i in range(T):
    time, direction = [x for x in input().split(' ')]
    queue.append([int(time), direction])

# for _ in map:
#     print(_)
# print()

# w a s d
cur_pos = [0,0,'d']
time = 0
trail = []
trail_len = 1
while True:
    
    # check if I have to move
    if len(queue) > 0 and queue[0][0] == time : 
        next_direction = queue.pop(0)[1]
        if next_direction == 'L':
            if cur_pos[2] == 'w':
                cur_pos[2] = 'a'
            
            elif cur_pos[2] == 'a':
                cur_pos[2] = 's'

            elif cur_pos[2] == 's':
                cur_pos[2] = 'd'

            elif cur_pos[2] == 'd':
                cur_pos[2] = 'w'
        
        if next_direction == 'D':
            if cur_pos[2] == 'w':
                cur_pos[2] = 'd'

            elif cur_pos[2] == 'a':
                cur_pos[2] = 'w'

            elif cur_pos[2] == 's':
                cur_pos[2] = 'a'

            elif cur_pos[2] == 'd':
                cur_pos[2] = 's'
    #print(cur_pos[1], cur_pos[0])
    
    if map[cur_pos[1]][cur_pos[0]] == '1':
        map[cur_pos[1]][cur_pos[0]] = '0'
        trail_len += 1
    trail.insert(0,cur_pos[:-1])

    #print(cur_pos, trail, trail_len)

    # move 
    cur_direction = cur_pos[2]

    if cur_direction == 'w':
        cur_pos[1] -= 1
    if cur_direction == 'a':
        cur_pos[0] -= 1
    if cur_direction == 's':
        cur_pos[1] += 1
    if cur_direction == 'd':
        cur_pos[0] += 1
    
    

    # check if it ends
    flag = False
    for i in range(trail_len):
        #print(cur_pos[:2], trail[i])
        
        if cur_pos[:2] == trail[i]:
            print(time+1)
            flag = True
            break
        if flag:
            break
    if flag:
        break
    if not (0 <= cur_pos[0] <= N-1 and 0 <= cur_pos[1] <= N-1 ):
        print(time+1)
        break
    
            
    #print()

    time += 1
"""
