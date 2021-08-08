"""
오큰수
https://www.acmicpc.net/problem/17298
"""

from collections import deque
import sys

def NGE(a, numList):
    for i, v in enumerate(numList):
        if a < v:
            return v
    return -1

N = int(input())
numList = deque(map(int, sys.stdin.readline().split()))

lastNum = 0
curNum = 0
curVal = 0
while numList:
    curNum = numList.popleft()
    
    if curVal == -1:
        curVal = NGE(curNum, numList)
        print(curVal, end=' ')
    elif lastNum > curNum:
        print(curVal, end=' ')
    else:
        curVal = NGE(curNum, numList)
        print(curVal, end=' ')
    
    lastNum = curNum
    
