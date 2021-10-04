"""
프린터
https://programmers.co.kr/learn/courses/30/lessons/42587
"""

def solution(priorities, location):
    answer = 1
    priorities[location] *= -1

    while priorities:
        print(priorities)
        # 맨 앞 원소 저장
        current_task = priorities[0]

        # 만약 해당 원소가 음수라면 우리가 찾아야할 것
        isMarked = False
        if current_task < 0:
            isMarked = True
            current_task *= -1

        executable = True
        for i in priorities:
            # 만약 해당 task보다 우선순위가 큰 task가 존재하면 맨 뒤로 보낸다.
            if current_task < abs(i):
                priorities.append(priorities[0])
                priorities.remove(priorities[0])
                executable = False
                break
        if executable:
            if isMarked:
                return answer
            else:
                answer += 1
                priorities.remove(priorities[0])


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))


# from queue import PriorityQueue

# def solution(priorities, location):
#     queue = []
#     maxIdx = 0
#     for i, p in enumerate(priorities):
#         queue.append([i, p])
#         if p > priorities[maxIdx]:
#             maxIdx = i
#     queue = queue[maxIdx:] + queue[:maxIdx]
#     # print(queue)

#     answer = 0
#     while True:
#         if queue:
#             maxPrior = max([x[1] for x in queue])
#         else:
#             break
#         for q in queue:
#             if q[1] == maxPrior:
#                 if q[0] == location:
#                     return answer+1
#                 queue.remove(q)
#                 break
#         answer += 1