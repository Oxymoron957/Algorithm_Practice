"""
뱀
https://www.acmicpc.net/problem/3190
"""

N = int(input())
K = int(input())

map = [['0']*N for _ in range(N)]

for i in range(K):
    x, y = [int(x) for x in input().split(' ')]
    map[x-1][y-1] = '1'

T = int(input())
queue = []
for i in range(T):
    time, direction = [x for x in input().split(' ')]
    queue.append([int(time), direction])

for _ in map:
    print(_)
print()

# w a s d
cur_pos = [0,0,'d']
time = 0
while True:
    # check if I have to move
    if queue[0][0] == time: 
        
        next_direction = queue.pop(0)[1]
        if next_direction == 'L':
            if cur_pos[2] == 'w':
                cur_pos[2] = 'a'
            if cur_pos[2] == 'a':
                cur_pos[2] = 's'
            if cur_pos[2] == 's':
                cur_pos[2] = 'd'
            if cur_pos[2] == 'd':
                cur_pos[2] = 'w'
        if next_direction == 'D':
            if cur_pos[2] == 'w':
                cur_pos[2] = 'd'
            if cur_pos[2] == 'a':
                cur_pos[2] = 'w'
            if cur_pos[2] == 's':
                cur_pos[2] = 'a'
            if cur_pos[2] == 'd':
                #print('check')
                cur_pos[2] = 's'
            
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
    if not (0 <= cur_pos[0] <= N and 0 <= cur_pos[1] <= N ):
        print(cur_pos)
        
        #print(time)
        break
    #print(cur_pos)
    time += 1

