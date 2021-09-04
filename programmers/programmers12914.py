"""
멀리뛰기
https://programmers.co.kr/learn/courses/30/lessons/12914
"""

import math

def solution(n):
    # 초기 1의 갯수와 2의 갯수 계산 
    numOne = 0 if n%2 ==0 else 1
    numTwo = n//2 if n%2 == 0 else (n-1)//2
    answer = 0

    while numTwo >= 0:
        # 경우의 수 분모 분자 계산 
        A = math.factorial(numOne + numTwo)
        B = math.factorial(numOne)*math.factorial(numTwo)
        answer += A//B  # factorial 계산에는 너무 커지므로 몫연산 
        # 1, 2의 갯수 증감 
        numTwo -= 1
        numOne += 2
    # 몫 반환 
    return int(answer%1234567)

print(solution(2000))