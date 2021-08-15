"""
계단을 오르는 방법
"""
from collections import deque
def solution(numOfStairs):
    answer = deque()
    dq = deque()
    dq.append([1])
    dq.append([2])
    dq.append([3])
    
    while dq:
        curStep = dq.pop()
        stepSum = sum(curStep)
        if stepSum < numOfStairs:
            if stepSum + 1 <= numOfStairs and curStep + [1] not in answer:
                dq.append(curStep + [1])
            if stepSum + 2 <= numOfStairs and curStep + [2] not in answer:
                dq.append(curStep + [2])
            if stepSum + 3 <= numOfStairs and curStep + [3] not in answer:
                dq.append(curStep + [3])            
        elif sum(curStep) == numOfStairs:
            answer.append(curStep)

    return len(answer)
for i in range(1, 50):
    print(solution(i))