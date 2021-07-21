"""
행렬 곱셈 순서
https://www.acmicpc.net/problem/11049
"""

# 입력 받기
numOfMatrix = int(input()) 
m = []
for i in range(numOfMatrix):
    m.append(list(map(int, input().split())))

# dp 배열 생성 
dp = [[0]*numOfMatrix for _ in range(numOfMatrix)]

# dp[i][j]를 계산하는데 사이에 k값을 사용하므로 1 차이나는 i, j 먼저 2 차이나는 i, j 다음, 3 차이나는 ... 이런식으로 호출한다. 
for e in range(1, numOfMatrix):
    for i in range(numOfMatrix-e):
        j = e+i # 계산할 dp[i][j] index 계산        
        dp[i][j] = 2**32 # 최댓값으로 초기화 
        for k in range(i, j): # 사이를 k로 쪼개고 최솟값인지 확인한다. 
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+m[i][0]*m[k][1]*m[j][1])

# 0 ~ numOfMatrix-1 까지의 최솟값 출력 
print(dp[0][numOfMatrix-1])