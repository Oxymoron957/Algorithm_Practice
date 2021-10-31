"""
불량 사용자
https://programmers.co.kr/learn/courses/30/lessons/64064
"""

def solution(user_id, banned_id):
    answers = []
    for bi in banned_id:
        same_names = []
        for ui in user_id:
            # 서로 길이가 다르면 무조건 다르다.
            if len(bi) != len(ui):
                continue
            else:
                idx = 0
                isEq = True
                # 각 idx의 요소가 같지 않으면 다르다.
                while idx != len(bi):
                    if bi[idx] == '*':
                        idx += 1
                        continue
                    if bi[idx] != ui[idx]:
                        isEq = False
                        break
                    idx += 1
                # 같으면 리스트에 넣는다.
                if isEq:
                    same_names.append(ui)
        print(bi, same_names)
        answers.append(same_names)

    # answers = list(map(tuple, answers))
    # print(list(set(answers)))    
    print(answers)
    answ = 0




print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rod*", "******"]))