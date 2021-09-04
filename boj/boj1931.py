"""
회의실 배정
https://www.acmicpc.net/problem/1931

※ 부족했던 점 : 
정렬을 통한 
"""

from collections import deque

N = int(input()) # 회의의 수 
I = [] # 회의 정보가 담긴 리스트
for i in range(N):
    I.append(list(map(int, input().split())))

I_sorted = sorted(I, key= lambda x: x[1], reverse = True)
# I_sorted = sorted(I, key= lambda x: x[1]-x[0], reverse = True)

# print(I_sorted)
answer = deque()
while I_sorted:
    candidate = I_sorted.pop()
    isAvailable = True
    # print(candidate)
    # print(answer)
    for start, end in answer:
        # print(start, end)
        # print()
        if ((candidate[0] <= start) and (candidate[1] <= start)) or ((candidate[0] >= end) and (candidate[1] >= end)):
            isAvailable = True
        else:
            isAvailable = False
            break

    if isAvailable:
        answer.append(candidate)

print(len(answer))