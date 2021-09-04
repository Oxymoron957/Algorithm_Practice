"""
가장 긴 증가하는 부분 수열
https://www.acmicpc.net/problem/11053
"""

N = int(input())
seq = list(map(int, input().split()))
# [현재 수열의 수, 최장 수열의 값]으로 자료구조를 수정한다.
answer = [[x, 1] for x in seq]

# 모든 element에 대해 검사
for i, v in enumerate(answer):
    # 처음 원소는 무조건 1의 값을 가지므로 pass
    if i == 0:
        continue
    else:
        # i 번째 원소 이전 원소들을 최장 수열의 값 순으로 나열한다.
        lastList = sorted(answer[:i], key= lambda x:x[1], reverse= True)
        # 나열한 원소 순으로 탐색한다.
        for n, l in lastList:
            # 해당 원소보다 크다면 해당 원소의 최장 수열값+1로 i번째 원소의 최장 수열값을 정한다.
            if v[0] > n:
                v[1] = l + 1
                break
# 최장 수열값이 가장 큰 원소 출력 
print(max([x[1] for x in answer]))