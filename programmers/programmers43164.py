"""
프로그래머스: 여행경로
https://programmers.co.kr/learn/courses/30/lessons/43164
"""

"""
DFS (깊이 우선 탐색)
Stack 자료구조를 사용하여 다음 노드로 돌아간다. (얼마나 깊이 들어왔는지 기억)
- 한붓 그리기 문제 

BFS (너비 우선 탐색)
Queue 자료구조를 사용하여 다음 노드로 돌아간다. (처음 노드가 어디있는지 기억)
"""

def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]

    print(routes)


solution([["ICN", "JFK"],["ICN", "IAD"], ["HND", "IAD"], ["JFK", "HND"]])



