"""
퇴사
https://www.acmicpc.net/problem/14501
"""

N = int(input())

cList = []
for _ in range(N):
    cList.append(tuple(map(int, input().split())))
print(cList)

dp = []
for n in range(N):
    candidate = []
    for i in range(len(dp)-1, -1, -1):
        print(n,i, cList[i])
        if cList[i][0] <= n-i:
            candidate.append(dp[i]+ cList[i][1])
    if not candidate:
        dp.append(0)
    else:
        dp.append(max(candidate))
    print(dp, candidate)
    print()

print(dp)