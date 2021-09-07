"""
오픈채팅방
https://programmers.co.kr/learn/courses/30/lessons/42888
"""

from collections import deque

def solution(record):
    users = {}
    dq = deque()

    for r in record:
        orders = r.split()
        if orders[0] == "Enter":
            dq.append("들어왔습니다. " + orders[1])
            users[orders[1]] = orders[2]
        elif orders[0] == "Leave":
            dq.append("나갔습니다. " + orders[1])
        elif orders[0] == "Change":
            users[orders[1]] = orders[2]

    answer = [] 
    while dq:
        user_info = dq.popleft().split()
        answer.append(users[user_info[1]]+ "님이 " + user_info[0])
    return answer

            

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))