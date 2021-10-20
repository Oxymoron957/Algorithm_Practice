"""
점프와 순간이동
https://programmers.co.kr/learn/courses/30/lessons/12980
"""

def solution(n):
    ans = 0
    
    while n != 0:
        if n%2 == 1:
            n -= 1
            ans += 1
        else:
            n = int(n/2)
    return ans


"""
def solution(n):
    ans = [0] * (n+1)

    for i in range(n+1):
        if i == 0:
            ans[i] = 0
        elif i==1:
            ans[i] = 1
        elif i==2:
            ans[i] = 1
        else:
            if i % 2 == 1:
                # print(i)
                ans[i] = ans[i-1] + 1
            else:
                ans[i] = ans[int(i/2)]

    return ans[-1]
"""

print(solution(5))
print(solution(6))
print(solution(5000))