"""
경주로 건설
https://programmers.co.kr/learn/courses/30/lessons/67259
"""

from collections import deque
from copy import deepcopy

def solution(board):
    map_size = len(board)-1
    dq = deque()
    dq.append([0,0,0,''])
    answer = []
    
    while dq:
        col, row, cost, lastDir = dq.popleft()

        # check if it ends
        if col == map_size and row == map_size:
            answer.append(cost)
        
        # move right / left / up / down 
        if row  +1 <= map_size and board[col][row+1] == 0:
            dq.append([col, row+1, cost + 100 if lastDir == 'right' or lastDir == '' else cost + 600, 'right'])
        if row-1 >= 0 and board[col][row-1] == 0:
            dq.append([col, row-1, cost + 100 if lastDir == 'left' or lastDir == '' else cost + 600, 'left'])
        if col+1 <= map_size and board[col+1][row] == 0:
            dq.append([col+1, row, cost + 100 if lastDir == 'down' or lastDir == '' else cost + 600, 'down'])
        if col-1 >= 0 and board[col-1][row] == 0:
            dq.append([col-1, row, cost + 100 if lastDir == 'up' or lastDir == '' else cost + 600, 'up'])
        board[col][row] = 2

        # for i in board:
        #     print(i)
        # print()

    return min(answer)
    # return answer





print(solution([[0,0,0],[0,0,0],[0,0,0]]), 900)
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]), 3800)
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]), 2100)
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]), 3200)  