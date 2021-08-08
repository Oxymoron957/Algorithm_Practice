"""
히스토그램
https://www.acmicpc.net/problem/1725
"""

import sys

N = int(sys.stdin.readline())
# histogram = list(map(int, input().split()))
h = []
for _ in range(N):
    h.append(int(sys.stdin.readline()))

# 이중 list 만들기 
# 

answer = []
for hval in h:
    # if not answer:
    #     answer.append([1])
    answer.append([hval])

    for i, ival in enumerate(answer):
        if ival[-1] == -1:
            continue
        if ival[0] > hval:
            ival.append(-1)
        else:
            ival.append(ival[-1]+ival[0])
print(answer)
