"""
AC 
https://www.acmicpc.net/problem/5430
"""

from collections import deque

T = int(input())

for i in range(T):
    p = deque(input())
    n = int(input())
    if n == 0:
        x = []
        input()
    else:
        x = deque(map(int, input()[1:-1].split(',')))
    
    delFront = True
    answer = True
    while p:
        command = p.popleft()
        if command == "R":
            delFront = not delFront
            continue
        if command == "D":
            if not x:
                answer = False
                print("error")
                break
            if delFront == True:
                x.popleft()
            else:
                x.pop()

    x = list(x)
    if not delFront:
        x = x[::-1]
    if answer:
        answerStr = "["
        for c in x:
            answerStr += (str(c) + ",")
        if len(answerStr) > 1:
            answerStr = answerStr[:-1]
        answerStr += "]"
        print(answerStr)
