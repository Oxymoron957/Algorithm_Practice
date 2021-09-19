"""
거리두기 확인하기
https://programmers.co.kr/learn/courses/30/lessons/81302
"""

from collections import deque

def isSafe(rowIdx, colIdx, room):
    dq = deque()
    dq.append([rowIdx, colIdx, 0])

    visited = set()
    visited.add((rowIdx, colIdx))
    while dq:
        # print(dq)
        curRow, curCol, curMove = dq.pop()
        if room[curRow][curCol] == 'P' and curRow != rowIdx and curCol != colIdx and curMove <= 2:
            # print(curRow, curCol, curMove)
            return False

        # move up 
        if curCol -1 >= 0 and room[curRow][curCol-1] != 'X' and (curRow, curCol-1) not in visited:
            visited.add((curRow, curCol-1))
            dq.append([curRow, curCol-1, abs(rowIdx-curRow)+abs(colIdx-(curCol-1))])     
        # move down 
        if curCol +1 <= 4 and room[curRow][curCol+1] != 'X' and (curRow, curCol+1) not in visited:
            visited.add((curRow, curCol+1))
            dq.append([curRow, curCol+1, abs(rowIdx-curRow)+abs(colIdx-(curCol+1))])
        # move left 
        if curRow -1 >= 0 and room[curRow-1][curCol] != 'X' and (curRow-1, curCol) not in visited:
            visited.add((curRow-1, curCol))
            dq.append([curRow-1, curCol, abs(rowIdx-(curRow-1))+abs(colIdx-curCol)])
        # move right
        if curRow +1 <= 4 and room[curRow+1][curCol] != 'X' and (curRow+1, curCol) not in visited:
            visited.add((curRow+1, curCol))
            dq.append([curRow+1, curCol, abs(rowIdx-(curRow+1))+abs(colIdx-curCol)])
        # print(dq)
    return True  
    

def solution(places):
    answer = []
    for room in places:
        safeRoom = True
        for rowIdx, rowData in enumerate(room):
            for colIdx, data in enumerate(rowData):
                if data == 'P' and not isSafe(rowIdx, colIdx, room):
                    safeRoom = False
        if safeRoom:
            answer.append(1)
        else:
            answer.append(0)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
