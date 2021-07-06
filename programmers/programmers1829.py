"""
카카오 프렌즈 컬러링북
https://programmers.co.kr/learn/courses/30/lessons/1829
"""

def bfs(pixel_value, y, x, m, n, picture, visited):
    count = 0 # 연결되고 같은 색상의 픽셀 수 
    queue = [[y,x]] # 주어진 pixel부터 시작한다.
    while queue: 
        cur_y, cur_x = queue.pop(0) # 다음 pixel을 꺼낸다. (BFS 방식으로)
        for i in [[-1,0], [1,0], [0,-1], [0,1]]: # 다음 픽셀의 상하좌우를 조사한다.
            new_y = cur_y + i[0]
            new_x = cur_x + i[1]
            
            if 0 <= new_y < m and 0 <= new_x < n: # 다음 픽셀의 상하좌우가 프레임 안이고
                if picture[new_y][new_x] == pixel_value and visited[new_y][new_x] != 1: # 픽셀값이 같고, 방문한 픽셀이 아닐경우
                    count += 1 # 픽셀 수를 증가시킨다.
                    visited[new_y][new_x] = 1 # 방문 표시를 한다.
                    queue.append([new_y,new_x]) # 같은 픽셀이므로 다음 픽셀로 넣는다.
    return count


def solution(m, n, picture):
    number_of_area = 0
    max_size_of_one_area = 0
    visited = [[0 for _ in range(m+1)] for _ in range(m+1)]

    for i in range(m):
        for j in range(n): # 모든 픽셀에 대해 조사한다. 
            if visited[i][j] != 1 and picture[i][j] != 0: # 방문하지 않고 픽셀값이 0이 아닌 픽셀에 대하여 
                max_size_of_one_area = max(bfs(picture[i][j], i, j, m, n, picture, visited), max_size_of_one_area) # BFS 탐색으로 해당 픽셀의 범위를 조사한다. 
                number_of_area += 1 # 범위가 가짓수를 증가시킨다. 

    return [number_of_area,max_size_of_one_area]

print(solution(6,4, [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]))


