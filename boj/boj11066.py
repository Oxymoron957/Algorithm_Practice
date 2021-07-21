"""
파일 합치기
https://www.acmicpc.net/problem/11066
"""

"""
합치는 파일이 연속적이어여야 된다!
1
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
"""

import sys
input = sys.stdin.readline
MAX = sys.maxsize

t = int(input())

def solve():
    n = int(input())
    file = list(map(int, input().split()))
    dp = [[0]*n for _ in range(n)]
    sum = [0]
    for f in file:
        sum.append(sum[-1]+f) # index-1의 값을 더한 sum을 가지는 배열
        
    for d in range(1,n): # 파일의 수 만큼 
        for i in range(n-d): # 남은 파일의 수 만큼
            j= d+i 
            dp[i][j] = MAX # dp[i][j] => i~j까지의 최소 합 
            for k in range(i,j): # 중간에 최소값이 존재하는 k가 있다면 dp[i][j]에 해당 답을 추가한다. 
                dp[i][j] = min(dp[i][j],dp[i][k]+dp[k+1][j]+sum[j+1]-sum[i]) 
    print(dp[0][n-1])

for i in range(t): 
    solve()

# T = int(input())

# for _ in range(T):
#     cost = 0
#     K = int(input())
#     num_arr = list(map(int, input().split()))
#     num_arr.sort()
#     print(num_arr)
#     index = 0
#     while True:
#         if index+2 >= len(num_arr): 
#             index = 0
#         if num_arr[index]+num_arr[index+1] > num_arr[index+2]:
#             cost += num_arr[index]+num_arr[index+1]
#             num_arr[index:index+2] = [num_arr[index]+num_arr[index+1]]
#             index += 1
#         else:
#             index = 0


#         if len(num_arr) <= 3:
#             cost += sum(num_arr)
#             print(cost)

        
#         print(num_arr, index)
#         K-=1

