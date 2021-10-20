"""
문자열 압축
https://programmers.co.kr/learn/courses/30/lessons/60057
"""

def tokenize(s, slice_):
    # slice 크기만큼 문자열을 잘라 보관한 리스트를 반환한다.
    result = []
    ptr = 0
    while ptr + slice_ <= len(s):
        result.append(s[ptr:ptr+slice_])
        ptr += slice_
    if s[ptr:] != '':
        result.append(s[ptr:])

    return result

def str_pressing(s_list):
    # 토큰 크기만큼 잘려진 문자열 리스트의 연속성을 조사한다.
    result = []
    ptr = 0
    row = 1
    while ptr < len(s_list) - 1:
        if s_list[ptr] == s_list[ptr+1]:
            ptr += 1
            row += 1
        else:
            result.append([s_list[ptr], row])
            ptr += 1
            row = 1
    result.append([s_list[ptr], row])
    ptr += 1
    row = 0
    # 연속성 정보를 바탕으로 압축된 문자열의 길이를 계산한다.
    answer = 0
    for i in result:
        if i[1] != 1:
            answer += len(str(i[1])) + len(i[0])
        else:
            answer += len(i[0])
    return answer

def solution(s):
    if len(s) == 1:
        return 1

    maxSlice = int(len(s)/2)

    # 모든 토큰 길이마다 적용한다.
    answer = float('inf')
    for i in range(1, maxSlice+1):
        s_list = tokenize(s, i)
        answer = min(answer, str_pressing(s_list))
    return answer

print(solution('a'))
print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))