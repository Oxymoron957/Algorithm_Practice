"""
탑
https://www.acmicpc.net/problem/2493
"""

N = int(input())
tops = list(map(int, input().split()))
stack = [] # [index, tower높이]
answer = []

for i in range(N):
    while stack: # 스택이 있을 경우
        if stack[-1][1] > tops[i]: # 수신 가능한 상황 (스택 마지막에 있는 타워의 높이 > 현재 타워의 높이)
            answer.append(stack[-1][0] + 1) # answer에 해당 인덱스를 추가한다. 
            break
        else:
            stack.pop() # 수신이 불가능하다면 스택 맨 위에 있는 타워는 pop시킨다. 
    if not stack:  # 스택이 비었을 경우 -> 왼쪽에 수신되는 것이 없으므로 anwser에 0을 푸시하여 최솟값을 넣는다.
        answer.append(0)
    stack.append([i, tops[i]])  # 스택에 [index, tower높이]를 넣는다.

print(" ".join(map(str, answer)))
