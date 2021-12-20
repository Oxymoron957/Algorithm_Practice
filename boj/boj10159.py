"""
저울
https://www.acmicpc.net/problem/10159
"""

from collections import deque

N = int(input())
M = int(input())

info = dict()
answer = dict()
for i in range(N):
    info[i+1] = [set(), set()]
    answer[i+1] = [set(), set()]

for i in range(M):
    bigger_than, lighter_than = map(int, input().split())
    info[bigger_than][0].add(lighter_than)
    info[lighter_than][1].add(bigger_than)

    answer[bigger_than][0].add(lighter_than)
    answer[lighter_than][1].add(bigger_than)
    
key_ = 1
while key_ < N+1:
    isNotFinished = False

    stack = deque()
    stack.append(key_)
    while stack:
        cur_key = stack.pop()
        print(answer, cur_key)
        
        if len(info[cur_key][0]) == 0:
            continue

        for i in list(info[cur_key][0]):
            if i not in answer[key_][0]:
                answer[key_][0].add(i)
                stack.append(i)
                isNotFinished = True


    if isNotFinished == False:
        key_ += 1
    # print(answer, key_)


