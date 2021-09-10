"""
거리두기 확인하기
https://programmers.co.kr/learn/courses/30/lessons/81302
"""

from collections import deque

def check(row, col, room):
    firLoc = [row, col]
    dq = deque()
    dq.append(firLoc)

    while dq:
        print(dq)
        curRow, curCol= dq.pop()

        print(row, col)
        if abs(row-curRow)+abs(col-curCol) > 2:
            print("over!")
            continue

        if curRow-1 >= 0:  
            if room[curRow-1][curCol] == 'P':
                return 0
            if room[curRow-1][curCol] == 'O':
                dq.append([curRow-1, curCol])
        if curRow+1 <= 4:  
            if room[curRow+1][curCol] == 'P':
                return 0
            if room[curRow+1][curCol] == 'O':
                dq.append([curRow+1, curCol])
        if curCol-1 >= 0:  
            if room[curRow][curCol-1] == 'P':
                return 0
            if room[curRow][curCol-1] == 'O':
                dq.append([curRow, curCol-1])
        if curCol+1 <= 4:  
            if room[curRow][curCol+1] == 'P':
                return 0
            if room[curRow][curCol+1] == 'O':
                dq.append([curRow, curCol+1])
    print()
    
    return 1

def solution(places):
    answer = []
    for room in places:
        isChecked = False
        for row, rowInfo in enumerate(room):
            for col, obj in enumerate(rowInfo):
                if obj == 'P' and not check(row, col, room):
                    isChecked = True
                    break
            
        if not isChecked:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer





print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
print(solution([["OOOOP", "PXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
