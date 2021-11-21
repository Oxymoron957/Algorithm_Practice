"""
처음과 끝이 이어져 있는 문자열을 상상해봅시다. 당신은 해당 문자열 내의 "같은 글자가 연속해 있는" 구간들을 추출하고자 합니다.

문자열 s가 매개변수로 주어집니다. s 내의 모든 "같은 글자가 연속해 있는" 구간의 길이를 각각 배열에 담아 오름차순으로 정렬하여 return 하도록 solution 함수를 완성해주세요.
"""

def solution(s):

    answer = [1] + [0]*999
    startIdx = 0
    for i in range(len(s)):
        if i != len(s)-1:
            if s[i] == s[i+1]:
                answer[startIdx] += 1
            else:
                startIdx += 1
                answer[startIdx] = 1
    answer = list(filter(lambda x:x!=0, answer))
    if s[0] == s[-1] and len(set(list(s))) > 1:
        answer[0]= answer[0] + answer[-1]
        answer.pop()

    return sorted(answer)


print(solution("aaabbaaa"))
print(solution("wowwow"))
print(solution("ababab"))
print(solution("baaaaaaaab"))




