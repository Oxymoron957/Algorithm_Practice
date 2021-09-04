"""
타일 채우기 
https://www.acmicpc.net/problem/2133

* 부족했던 점
- 점화식을 도출했으나 그것을 더 잘게 분해하지 못했다.
- 2, 4, 6까지만 계산한 결과를 토대로 점화식을 세우려해서 확실함이 부족했다. (8까지 계산해봐야 했었다.)
- dp[0]이 1이라고 생각하지 못했다. 
"""

# input
N = int(input())

# varialbes
tiles = [0] * 31
tiles[0] = 1
tiles[2] = 3
for n in range(4, N+1, 2):
    for i in range(n-2, -1, -2):
        tiles[n] += tiles[i] * 3 if i == n-2 else tiles[i] * 2 

if N == 1:
    print(0)
else:
    print(tiles[N])

