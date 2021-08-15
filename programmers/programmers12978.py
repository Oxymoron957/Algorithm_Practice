"""
배달
https://programmers.co.kr/learn/courses/30/lessons/12978
"""

from collections import deque

def solution(N, road, K):
    nodes = {}
    for r in road:
        if nodes.get(r[0]) is None:
            nodes[r[0]] = [[r[1], r[2]]]
        else:
            nodes[r[0]].append([r[1], r[2]])
            
        if nodes.get(r[1]) is None:
            nodes[r[1]] = [[r[0], r[2]]]
        else:
            nodes[r[1]].append([r[0], r[2]])

    # print(nodes)
    q = deque()
    q.append([1, K])

    visited = set()
    visited.add(1)

    while q:
        curNode, curCost = q.pop()

        nextNodes = nodes[curNode]
        for n in nextNodes:
            if curCost - n[1] >= 0:
                q.append([n[0], curCost - n[1]])
                visited.add(n[0])
        
    return len(visited)



print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))

