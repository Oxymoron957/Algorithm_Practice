"""
124 나라의 숫자
https://programmers.co.kr/learn/courses/30/lessons/12899

* 부족했던 점 : 
진수 변환에 약한 것 같다. 
"""


def solution(n):
    references = [4, 1, 2]
    numList = []
    
    # 3진법 변환 loop 
    while n // 3 > 0:
        # 3으로 나뉘어 떨어지는 경우 1을 뺀다.
        if n % 3 == 0:
            numList.append(n % 3)
            n = n - 1
        # 그렇지 않을경우 정상적으로 진법 변환
        else:
            numList.append(n % 3)
        # n update
        n = n // 3
    # list에 추가한다.
    if n != 0:
        numList.append(n)

    # 1,2,4 나라에 맞게 변환
    answer = []
    for i in numList[::-1]:
        if i == 0:
            answer.append(str(references[i]))
        elif i == 1:
            answer.append(str(references[i]))
        elif i == 2:
            answer.append(str(references[i]))

    return ''.join(answer)

print(solution(20))