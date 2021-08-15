"""
뉴스 클러스터링
https://programmers.co.kr/learn/courses/30/lessons/17677
"""

def createToken(str):
    strList = []
    for i in range(len(str)-1):
        token = str[i:i+2].lower()
        if token.isalpha():
            strList.append(token)
    return strList

def getElementNum(strList):
    strDict = {}
    for token in strList:
        if strDict.get(token) is None:
             strDict[token] = 1
        else:
            strDict[token] += 1
    return strDict

def solution(str1, str2):
    # 두 글자씩 나누어 element 생성하기 
    str1List = createToken(str1)
    str2List = createToken(str2)
    
    # 각 element의 갯수 구하기 
    str1Dict = getElementNum(str1List)
    str2Dict = getElementNum(str2List)

    # 교집합 element 구하기
    interElement = list(set(str1List) & set(str2List))
    unionElement = list(set(str1List) | set(str2List))
    
    # 중복된 element의 갯수 구하기
    minVal = []
    maxVal = []
    for i in list(interElement):
        minVal += (min(str1Dict[i], str2Dict[i])-1) * [i]
        maxVal += (max(str1Dict[i], str2Dict[i])-1) * [i]

    print(interElement, unionElement)
    print(minVal, maxVal)
    if len(unionElement) == 0:
        return 65536
    elif len(interElement) == 0:
        return 0
    else:
        return int(((len(interElement+minVal))/(len(unionElement+maxVal)))*65536)


print(solution("FRANCE","french"))
print(solution("handshake","shake hands"))
print(solution("aa1+aa2","AAAA12"))
print(solution("E=M*C^2","e=m*c^2"))
print(solution("aa1+aa2","AA12"))
print(solution("aabbc","abbcde"))

