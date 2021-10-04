"""
이진 변환 반복하기
https://programmers.co.kr/learn/courses/30/lessons/70129
"""

def solution(s):
    zeroes = 0
    count = 0
    while s != '1':
        count += 1
        zeroes += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
    # print(zeroes, count)
    return [count, zeroes]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))

