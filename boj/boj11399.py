"""
ATM
https://www.acmicpc.net/problem/11399
"""

N = int(input())
P = list(map(int, input().split()))

# print(N, P)

P_sorted = sorted(P)
# print(P_sorted)

answer = 0
for i, v in enumerate(P_sorted):
    answer += sum(P_sorted[:i+1])
print(answer)