"""
위장
https://programmers.co.kr/learn/courses/30/lessons/42578
"""

def solution(clothes):
    cloth_info = dict()
    for cloth, category in clothes:
        if cloth_info.get(category) == None:
            cloth_info[category] = [cloth]
        else:
            cloth_info[category].append(cloth)
    answer = 1
    for i in [len(x)+1 for x in cloth_info.values()]:
        answer *= i
    return answer-1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
