"""
뉴스 클러스터링
https://programmers.co.kr/learn/courses/30/lessons/17677

※ 부족했던 점
파이썬 collections 라이브러리의 Counter 클래스에 대해서 알지 못했다. 

Counter 클래스 : 
    1. 데이터의 갯수를 셀 때 유용하다. -> Container 안의 element의 갯수를 가지고 있는 자료구조를 만들 수 있다.
    2. set 자료형처럼 집합 연산이 가능하다. 
        - 교집합 : 서로 가지고 있는 element와 해당 element의 갯수 중 작은 수를 저장
        - 합집합 : 모든 element와 해당 element의 갯수 중 큰 수를 저장

"""

from collections import Counter

def createToken(str):
    strList = []
    for i in range(len(str)-1):
        token = str[i:i+2].lower()
        if token.isalpha():
            strList.append(token)
    return strList

def solution(str1, str2):
    # 두 글자씩 나누어 element 생성하기 
    str1List = createToken(str1)
    str2List = createToken(str2)

    # 각 문자열의 Counter 객체 생성 
    str1Counter = Counter(str1List)
    str2Counter = Counter(str2List)
    
    # 합집합과 교집합 생성 
    intersection = list((str1Counter & str2Counter).elements())
    union = list((str1Counter | str2Counter).elements())

    # 자카드 유사도 계산 및 반환
    if len(union) == 0 and len(intersection) == 0:
        return 65536
    else:
        return int(len(intersection) / len(union) * 65536)
    




print(solution("FRANCE","french"))
print(solution("handshake","shake hands"))
print(solution("aa1+aa2","AAAA12"))
print(solution("E=M*C^2","e=m*c^2"))
print(solution("aa1+aa2","AA12"))
print(solution("aabbc","abbcde"))

