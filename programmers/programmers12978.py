"""
배달
https://programmers.co.kr/learn/courses/30/lessons/12978

※ 부족했던 점
BFS에서 한층 더 효율적인 다익스트라 알고리즘을 적용하지 못했다. 
"""

from collections import deque

def solution(N, road, K):
    # 각 Node에 대한 최단 거리 정보 생성 (from Node 1 to last Node)
    distances = {1:0}
    for n in range(2, N+1):
        distances[n] = float('inf')
    
    # 각 Node에 대한 연결 정보 생성 (target node와 distance)
    nodes = {}
    for v1, v2, d in road:
        nodes[v1] = nodes.get(v1, []) + [(v2, d)]
        nodes[v2] = nodes.get(v2, []) + [(v1, d)]
    
    # 다익스트라 알고리즘으로 Node 탐색 시작
    queue  = deque()
    queue.append(1)
    while queue:
        curNode = queue.popleft()
        for nextNode, d in nodes[curNode]:
            # nextNode에서부터 node 1까지의 거리가 더 짧다면 거리를 갱신한다.
            if distances[nextNode] > distances[curNode] + d:
                distances[nextNode] = distances[curNode] + d
                queue.append(nextNode)
                
    return len([x for x in distances.values() if x <= K])

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))

