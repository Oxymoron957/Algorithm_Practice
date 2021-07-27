"""
외벽 점검
https://programmers.co.kr/learn/courses/30/lessons/60062
"""

from types import WrapperDescriptorType


def minDist(n, pointA, pointB):
    return min(abs(pointA-pointB), n-abs(pointA-pointB))

def solution(n, weak, dist):
    if len(weak) == 1 and len(dist) > 0:
        return 1
    distList = []
    for i in range(len(weak)):
        if i == len(weak)-1:
            distList.append(minDist(n, weak[i], weak[0]))
        else:
            distList.append(minDist(n, weak[i], weak[i+1]))
    distList.sort(reverse=True)
    dist.sort(reverse = True)
    print(distList)
    for i in range(len(dist)): # i명으로 가능해?
        costList = distList[i+1:]
        costListIdx = 0
        workerIdx = 0
        while True:
            if dist[workerIdx] - costList[costListIdx] >= 0:
                dist[workerIdx] -= costList[costListIdx]
                costListIdx += 1
                continue
            workerIdx += 1
            
            if workerIdx >= len(dist)-1:
                break
            if costListIdx >= len(costList)-1:
                return workerIdx
        
    return -1



print(solution(8, [1,3,5,7,8], [2,3]))
