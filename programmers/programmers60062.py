"""
외벽 점검
https://programmers.co.kr/learn/courses/30/lessons/60062
"""

def solution(n, weak, dist):
    dist.sort(reverse = True)
    workersCapPoints = [()]

    # 각 worker에 대하여
    for worker, workerCap in enumerate(dist):
        workerCapPoints = []
        # 각자가 고칠 수 있는 부분을 set list로 도출한다. 
        for idx, weakpoint in enumerate(weak):
            dest = weak[idx:] + [n + x for x in weak[:idx]]
            canGo = [x % n for x in dest if x - weakpoint <= workerCap]
            workerCapPoints.append(set(canGo))
        
        # 지금까지의 경우의 수가 담긴 set list에 더해서 모두 방문 가능한지 검사한다.
        newWorkersCapPoints = set()
        for workerCapPoint in workerCapPoints:
            for workersCapPoint in workersCapPoints:
                newCapPoints = workerCapPoint | set(workersCapPoint)
                if len(newCapPoints) == len(weak):
                    return worker+1
                newWorkersCapPoints.add(tuple(newCapPoints))
        workersCapPoints = newWorkersCapPoints

    return -1

print(solution(12, [1, 5, 6, 10], [1,2,3,4]))
