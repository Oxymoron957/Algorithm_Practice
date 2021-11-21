"""


"""

def check(answer):
    for row in answer:
        if 0 in row:
            return True
    return False

def solution(rows, columns):
    answer = [[0]*columns for _ in range(rows)]

    if max(rows, columns) % min(rows, columns) == 0:
        r, c = 0, 0
        num = 1
        while True:
            answer[r][c] = num
            if num%2 == 0:
                r = r+1 if r != rows-1 else 0
            if num%2 == 1:
                c = c+1 if c != columns-1 else 0
            num += 1

            if r == 0 and c == 0:
                break
    
    else:
        r, c = 0, 0
        num = 1
        while check(answer):
            answer[r][c] = num
            if num%2 == 0:
                r = r+1 if r != rows-1 else 0
            if num%2 == 1:
                c = c+1 if c != columns-1 else 0
            num += 1
    
    return answer


print(solution(3,6))