"""
인구 이동
https://www.acmicpc.net/problem/16234
"""

N, L, R = map(int, input().split())
land = []
for i in range(N):
    land.append(list(map(int, input().split())))

day = 0
workingList = []
while True:
    notMoved = True

    # 현재 방문해야하는 좌표가 담긴 리스트 생성
    for i in range(N):
        for j in range(N):
            workingList.append([i,j])

    groupOfUnion = []
    # 다음에 방문해야하는 좌표가 존재할 때
    while workingList:
        queue = []
        queue.append(workingList.pop()) # 방문해야하는 queue를 초기화한다. 
        u = [] # 이미 방문한(국경을 개방한) 좌표를 저장한다.
        while queue:
            # print(queue)
            workingTile = queue.pop(0) # 현재 조사하고 있는 좌표 초기화
            
            # 상하좌우를 조사하며 인구수가 조건에 맞는지 조사 -> 맞다면 u에 추가한다. 
            if workingTile[1] > 0 and L <= abs(land[workingTile[0]][workingTile[1]] - land[workingTile[0]][workingTile[1]-1]) <= R:
                if not [workingTile[0],workingTile[1]-1] in u:
                    u.append([workingTile[0],workingTile[1]-1])
                    queue.append([workingTile[0],workingTile[1]-1])
                if [workingTile[0],workingTile[1]-1] in workingList:
                    workingList.remove([workingTile[0],workingTile[1]-1])
            if workingTile[1] < N-1 and L <= abs(land[workingTile[0]][workingTile[1]] - land[workingTile[0]][workingTile[1]+1]) <= R:
                if not [workingTile[0],workingTile[1]+1] in u:
                    u.append([workingTile[0],workingTile[1]+1])
                    queue.append([workingTile[0],workingTile[1]+1])
                if [workingTile[0],workingTile[1]+1] in workingList:
                    workingList.remove([workingTile[0],workingTile[1]+1])
            if workingTile[0] > 0 and L <= abs(land[workingTile[0]][workingTile[1]] - land[workingTile[0]-1][workingTile[1]]) <= R:
                if not [workingTile[0]-1,workingTile[1]] in u:
                    u.append([workingTile[0]-1,workingTile[1]])
                    queue.append([workingTile[0]-1,workingTile[1]])
                if [workingTile[0]-1,workingTile[1]] in workingList:              
                    workingList.remove([workingTile[0]-1,workingTile[1]])
            if workingTile[0] < N-1 and L <= abs(land[workingTile[0]][workingTile[1]] - land[workingTile[0]+1][workingTile[1]]) <= R:
                if not [workingTile[0]+1,workingTile[1]] in u:
                    u.append([workingTile[0]+1,workingTile[1]])
                    queue.append([workingTile[0]+1,workingTile[1]])
                if [workingTile[0]+1,workingTile[1]] in workingList:
                    workingList.remove([workingTile[0]+1,workingTile[1]])
        groupOfUnion.append(u)

    # 국경 개방한 좌표를 모두 조사한 후엔, 인구를 합친다. 
    for u in groupOfUnion:
        totalUnionPeople = 0
        for i in u:
            totalUnionPeople += land[i[0]][i[1]]
        for i in u:
            land[i[0]][i[1]] = int(totalUnionPeople/len(u))
            notMoved = False

    if notMoved:
        print(day)
        break
    else:
        day+=1
    