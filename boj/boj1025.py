"""
제곱수 찾기
https://www.acmicpc.net/problem/1025
"""

from math import sqrt

N, M = list(map(int, input().split()))

matrix = []
for i in range(N):
    matrix.append(list(input()))

answer = -1

# 각 원소에 대해서 조사
for n in range(N):
    for m in range(M): 
        # 행/열에 대한 jump 값 정의
        for n_jump in range(-N, N):
            for m_jump in range(-M, M):
                # jump 값이 0이면 continue
                if n_jump == 0 and m_jump == 0:
                    continue
                
                # 현재 이어붙일 행/열 값
                row = n
                col = m
                
                # 현재 step과 value
                step = 0
                value = ''
                
                while (0 <= row < N) and (0 <= col < M):
                    # 이어붙인다
                    value += str(matrix[row][col])
                    step += 1
                    # 제곱근이 정수고 원래 answer보다 크다면 교체
                    if sqrt(int(value)) - int(sqrt(int(value))) == 0 and int(value) > answer:
                        answer = int(value)
                    # row, col 갱신
                    row = n + step*n_jump
                    col = m + step*m_jump
print(answer)



