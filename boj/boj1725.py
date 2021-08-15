"""
히스토그램
https://www.acmicpc.net/problem/1725
"""

import sys
from collections import deque

# input
SIZE = int(sys.stdin.readline())
HISTO = []
for _ in range(SIZE):
    HISTO.append(int(sys.stdin.readline()))
HISTO.append(0)
SIZE+=1

# variables
st = deque()
answer = -1
curIdx = 1

while curIdx <= SIZE-1:
    if not st:
        st.append(curIdx)
        continue

    while HISTO[st[-1]] > HISTO[curIdx]:
        idx = st.pop()
        if len(st) == 0:
            answer = max((curIdx)*HISTO[idx], answer)
            break    
        answer = max((curIdx - st[-1] - 1)*HISTO[idx], answer)

    st.append(curIdx)
    curIdx+=1

print(answer)

