"""
퇴사
https://www.acmicpc.net/problem/14501
"""

N = int(input())

dp = [0] * (N+1)
T = []
P = []

for _ in range(N):
    input_ = list(map(int, input().split()))
    T.append(input_[0])
    P.append(input_[1])

# print(T, P)

# 거꾸로 생각하자 
for day in range(N-1, -1, -1):
    # 만약 day+T[day] > N 이라면 그 다음날과 cost가 같도록
    # print(N, day, T[day], P[day])
    if day + T[day] > N:
        dp[day] = dp[day+1]
    # day에 상담을 하지 않고 다음날로 넘어갈 경우, day에 상담을 해서 Pay를 받고 점프를 할 경우 비교 
    else: 
        dp[day] = max(dp[day+1], dp[day+T[day]]+P[day]) 

print(dp[0])