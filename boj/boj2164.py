"""
카드2
https://www.acmicpc.net/problem/2164
"""

from typing import Deque


num = int(input())  

numList = Deque()
for i in range(1, num+1):
    numList.append(i)

while len(numList) != 1: 
    numList.popleft()
    numList.append(numList.popleft())
    # print(numList)

print(numList[0])