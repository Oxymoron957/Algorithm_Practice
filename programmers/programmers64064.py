"""
불량 사용자
https://programmers.co.kr/learn/courses/30/lessons/64064
"""

from itertools import permutations

def check(candidate, banned_id):
    for i in range(len(banned_id)):
        if len(candidate[i]) != len(banned_id[i]):
            return False
        
        for j in range(len(banned_id)):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != candidate[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    candidates = list(permutations(user_id, len(banned_id)))
    banned_users = []
    for candidate in candidates:
        if check(candidate, banned_id):
           candidate = set(candidate)
           if candidate not in banned_users:
               banned_users.append(candidate)

    return len(banned_users)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rod*", "******"]))