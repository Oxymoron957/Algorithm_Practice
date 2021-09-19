"""
경사로
https://www.acmicpc.net/problem/14890
"""

# input 
N, L = list(map(int, input().split()))
routes = []
mapData = []
for i in range(N):
    row = list(map(int, input().split()))
    mapData.append(row)
    routes.append(row)
for j in range(N):
    colRoutes = []
    for i in range(N):
        colRoutes += [mapData[i][j]]
    routes.append(colRoutes)

# 2N개의 Route를 하나씩 검사한다.
answer = 0
# for route in routes:
for route in [[3, 2, 2, 2, 3, 3], [3,2,2,1,1,1]]:
    coor = 1 # 검사할 다음 Block
    height = route[0] # 현재 높이
    while True:
        print(coor, route[coor], height)
        
        # 끝까지 도달했을 경우 break
        if coor == N-1:
            print(route)
            answer += 1
            break

        # 다음 Block이 높이가 같을 경우 
        # -> 다음 Block으로 이동한다.
        if route[coor] == height:
            coor += 1

        
        # 현 위치가 더 낮을 경우
        elif route[coor+1] - height == 1:
            # L만큼의 평지가 확보되어있는지 확인    
            constructable = True
            for i in range(L):
                if coor-i+1 > L and (route[coor-i+1] == -1 or route[coor-i+1] != height):
                    constructable = False
            if constructable:
                height += 1
            else:
                break

        # 현 위치가 더 높을 경우
        elif route[coor+1] - height == -1:
            # print('called')
            # L만큼의 평지가 확보되어있는지 확인
            constructable = True
            for i in range(L):
                route[coor+i+1] = -1
                # print(route[coor+i+1], height-1)
                if route[coor+i+1] != height-1:
                    constructable = False
            if constructable:
                coor += L
                height -= 1
            else:
                break
        # 다음 Block의 높이가 1보다 클 경우
        # -> break 
        else:
            break

print(answer)        
