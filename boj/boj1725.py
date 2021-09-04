"""
히스토그램
https://www.acmicpc.net/problem/1725

※ 부족했던 점 : 
스택의 원리로 푸는 문제임은 파악했으나 스택을 비우는 조건을 파악하는 능력은 아직 부족한 것 같다.
"""

import sys
from collections import deque

# input
SIZE = int(sys.stdin.readline())
HISTOGRAM = []
for _ in range(SIZE):
    HISTOGRAM.append(int(sys.stdin.readline()))

# variables 
stack = deque()
answer = 0

for i in range(SIZE):
    # 이번 그래프의 높이가 스택에 저장된 마지막 높이보다 작을 경우 -> 스택에서 꺼내서 넓이 계산 후 최대 넓이 후보군에 넣는다.
    while len(stack) != 0 and HISTOGRAM[stack[-1]] > HISTOGRAM[i]:
        # 스택을 pop해서 높이 정보를 빼온다. 
        height_histogram = stack.pop()

        # 가장 마지막 스택까지 pop 했을 경우
        if len(stack) == 0:
            width = i
        # 아닐경우는 계산 
        else:
            width = i - stack[-1] -1
        
        answer = max(answer, width * HISTOGRAM[height_histogram])
    
    stack.append(i)

# 마지막 histogram을 계산 후에 스택에 원소가 남아있다면 비워준다. (최대 넓이를 계산해서 후보군과 비교한다.)
while len(stack) != 0:
    # 스택을 pop해서 높이 정보를 빼온다. 
    height_histogram = stack.pop()

    # 가장 마지막 스택까지 pop 했을 경우 
    if len(stack) == 0:
        width = SIZE
    else:
        width = SIZE - stack[-1] -1
    
    answer = max(answer, width * HISTOGRAM[height_histogram])

print(answer)