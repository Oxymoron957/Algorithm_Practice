"""
병든 나이트
https://www.acmicpc.net/problem/1783

※ 부족했던 점 : 
1,4번 move를 반복하는 것이 최대의 효율을 내는 것임은 캐치했으나 시뮬레이션이 아닌 그리디 알고리즘을 통해 바로 답을 구하는 법을 생각하지 못했다. 
"""

N, M = list(map(int, input().split()))


# 세로의 길이가 1 => 시작 위치에서 끝
if N == 1:
    blocks = 1 
# 세로 길이가 2 => 1, 4번 move를 할 수 없으므로 최대 4 혹은 (M-1)//2+1 값을 갖는다.
elif N == 2:
    blocks = min(4, (M-1)//2 + 1) 
# 가로 길이가 6 이하일 경우, 4개의 move를 모두 할 수 없으므로 M혹은 최대 4값을 갖는다.
elif M < 7: 
    blocks = min(4, M) 
# 나머지 경우 2,3번 move를 한번 하고, 1,4번 move를 반복하는 것이 최대의 효율을 갖는다.
else: 
    blocks = (2 + (M-5)) + 1 

print(blocks)



