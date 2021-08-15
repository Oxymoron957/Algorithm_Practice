"""
가짜 영수증 찾기
"""

def solution(amountText):
    if not amountText:
        return False
    digits = amountText.split(',')
    print(digits)
    if len(digits) == 1 and len(digits[0]) != 1 and digits[0][0] == '0':
        return False
    for i, d in enumerate(digits):
        if not d.isnumeric():
            return False
        elif i != 0 and len(d) != 3:
            return False
        elif i == 0 and d[0] == '0':
            return False

    return True
        


print(solution(",,,"))
print(solution("0,000"))
print(solution("100,00"))
print(solution("00"))
print(solution("0"))
print(solution(""))
print(solution("30"))
print(solution("10,$000"))
print(solution("039900"))


