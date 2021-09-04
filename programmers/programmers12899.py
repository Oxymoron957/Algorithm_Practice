"""
124 나라의 숫자
https://programmers.co.kr/learn/courses/30/lessons/12899
"""


def solution(n):
    # 몇 자리가 필요한지 계산
    digits = [3]
    while sum(digits) < n:
        digits.append(digits[-1]*3)

    answer = ''
    print(digits)

    while digits:
        cur_digit = int(digits.pop()/3)

        if cur_digit == 1:
            answer += str(n)
            break
        print(n, cur_digit)
        if n % cur_digit != 0:
            cur_num = n // cur_digit 
            n -= cur_num * cur_digit
        else:
            cur_num = n // cur_digit-1
            n -= cur_num * cur_digit
            
        answer += str(cur_num)

    return answer.replace('3','4')


# for n in range(1, 30):
#     print(solution(n))

print(solution(20))
