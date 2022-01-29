"""
오르막 수
https://www.acmicpc.net/problem/11057
"""

n = int(input())

cur = [1,1,1,1,1,1,1,1,1,1]
next_ = [0]*10
for i in range(n-1):
    for j in range(10):
        next_[j] = sum(cur[j:]) # next 
    cur = next_
    next_ = [0]*10


print(sum(cur)%10007)
