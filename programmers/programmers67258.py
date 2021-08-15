"""
보석 쇼핑 20210810
https://programmers.co.kr/learn/courses/30/lessons/67258

※ 부족했던 부분
    딕셔너리의 key:value를 활용하는 스킬이 부족했던 것 같다.
    이번 문제처럼 각 element의 갯수를 최적화하는 문제에서 element의 갯수를 value로 보관하여 증가 및 감소시켜 최적해를 구할 수 있다. 
"""

def solution(gems):
    numOfGems = len(set(gems))
    answer = []
    start, end = 0, 0
    gemDict = {gems[0]: 1}
    while start < len(gems) and end < len(gems):
        # print(gemDict)
        # 모든 종류의 보석을 가지고 있을 경우 -> start를 늘려가며 최소 구간을 구한다.
        if len(gemDict) == numOfGems:
            answer.append([start, end, end-start])
            # start의 보석의 갯수가 1개일 경우 0으로 줄어듦으로 삭제한다. (중요)
            if gemDict[gems[start]] == 1:
                del gemDict[gems[start]]
            else:
                gemDict[gems[start]] -= 1
            start += 1
            
        # 모든 종류의 보석을 가지고 있지 않을 경우 -> end를 늘려가며 보석의 갯수를 늘린다.
        else:
            end+=1
            if end == len(gems):
                break
            if gemDict.get(gems[end]) is None:
                gemDict[gems[end]] = 1
            else:      
                gemDict[gems[end]] += 1 
    answer.sort(key=lambda x:x[2])
    return answer[0][0]+1, answer[0][1]+1
            

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution(["RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "RUBY", "DIA", "EMERALD", "SAPPHIRE"]))
