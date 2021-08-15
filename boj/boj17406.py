"""
배열돌리기4
https://www.acmicpc.net/problem/17406


※ 부족했던 부분
배열로 표현된 맵을 조작하는 구현 능력이 아직 낮다는 것을 느꼈다. 
"""
from itertools import permutations
from copy import deepcopy

# input 
N, M, K = list(map(int, input().split()))
arr = []
q = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
for _ in range(K):
    q.append(list(map(int, input().split())))

# rotate 함수
def rotate(arr, q_list):
    for q in q_list:
        startPoint = [q[0] - q[2] -1, q[1] - q[2] -1]
        endPoint = [q[0] + q[2] -1, q[1] + q[2] -1]

        while startPoint[0] < endPoint[0] and startPoint[1] < endPoint[1]:
            corner1, corner2, corner3 = arr[startPoint[0]][endPoint[1]], arr[endPoint[0]][endPoint[1]], arr[endPoint[0]][startPoint[1]] 
            
            for x in range(endPoint[1], startPoint[1], -1): 
                arr[startPoint[0]][x] = arr[startPoint[0]][x-1]

            for x in range(endPoint[0], startPoint[0], -1): 
                arr[x][endPoint[1]] = arr[x-1][endPoint[1]]

            for x in range(startPoint[1], endPoint[1], 1): 
                arr[endPoint[0]][x] = arr[endPoint[0]][x+1]

            for x in range(startPoint[0], endPoint[0], 1): 
                arr[x][startPoint[1]] = arr[x+1][startPoint[1]]

            arr[startPoint[0]+1][endPoint[1]], arr[endPoint[0]][endPoint[1]-1], arr[endPoint[0]-1][startPoint[1]] = corner1, corner2, corner3 

            startPoint[0], startPoint[1] = startPoint[0]+1, startPoint[1]+1
            endPoint[0], endPoint[1] = endPoint[0]-1, endPoint[1]-1
    
    return arr
                    

# 가능한 모든 queue 만들기
q_list = tuple(permutations(q))

# arr deep copy 후, 함수에 arr과 queue 전달
minValue = 2**32 
for scence in q_list:
    result = rotate(deepcopy(arr), scence)
    
    # 최솟값 갱신
    for row in result:
        minValue = min(sum(row), minValue)

print(minValue) 



li = [[1], [2], [3], [4]]
queueGenerated = list(permutations(li))
print(queueGenerated)