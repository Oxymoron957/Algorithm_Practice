"""
n 진수 게임
https://programmers.co.kr/learn/courses/30/lessons/17687

"""

def calculate_n(n, q):
    if n == 0:
        return ["0"]

    rev_base = []

    while n > 0:
        n, mod = divmod(n, q)
        rev_base.append(str(mod))
    
    for i, num in enumerate(rev_base):
        if num == '10':
            rev_base[i] = 'A'
        elif num == '11':
            rev_base[i] = 'B'
        elif num == '12':
            rev_base[i] = 'C'
        elif num == '13':
            rev_base[i] = 'D'
        elif num == '14':
            rev_base[i] = 'E'
        elif num == '15':
            rev_base[i] = 'F'
        
    return rev_base[::-1] 


def solution(n, t, m, p):
    arr = []
    answer = []
    i = 0
    turn = 0
    while t > 0:
        arr.extend(calculate_n(i, n))
        i += 1
        if len(arr) > p-1+m*turn:
            #print(arr, p-1+m*turn)
            answer.append(arr[p-1+m*turn])
            turn += 1
            t -= 1
    return ''.join(answer)


print(solution(16,16,2,1))
