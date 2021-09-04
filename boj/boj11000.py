"""
강의실 배정
https://www.acmicpc.net/problem/11000

# 몰랐던 점 : 
heapq 모듈
-> 이진 트리(binary tree) 기반의 최소 힙(min heap) 자료구조를 제공
heapq.heappush, heapq.heapppop를 통해 언제나 정렬된 상태로 리스트를 유지할 수 있다.
이번 문제에서 리스트는 해당 강의실이 끝나는 시간을 기준으로 정렬되어야 효율적인 비교를 할 수 있으므로 필요하다. 
"""


import heapq

# input
N = int(input())
lectureTime = []
for _ in range(N):
    lectureTime.append(list(map(int,input().split())))

# 시간표를 시작 시간 기준으로 정렬한다.
lectureTime.sort(key=lambda x:x[0])

# 강의실을 저장하는 리스트
queue = []
# heapq를 통해서 queue에 시간표의 endtime을 정렬된 상태로 저장한다. 
heapq.heappush(queue,lectureTime[0][1])

# lecture time을 모두 방문한다.
for i in range(1,N):
    
    # 만약 queue의 끝나는 시간이 이번 lecture time이 start time보다 크다면 강의실에 수용하지 못하므로 강의실의 수를 늘린다. (정렬된 상태로)
    if queue[0] > lectureTime[i][0]:
        heapq.heappush(queue,lectureTime[i][1])
    else:
    # 만약 수용 가능하다면 해당 queue를 제거하고 이번 lecture time의 endtime으로 다시 push한다.(정렬된 상태 유지)
        heapq.heappop(queue)
        heapq.heappush(queue,lectureTime[i][1])
    # print(queue)

print(len(queue))

