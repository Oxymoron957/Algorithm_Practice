"""
연속합
https://www.acmicpc.net/problem/1912
"""

# input
n = int(input())
arr = list(map(int, input().split()))

# print(n, arr)

# case1 음수 양수가 섞여있을때
if max(arr) > 0 and min(arr) < 0:
    idx = 0
    cur = 0
    candidate = []
    while idx < n:
        # 지금까지의 합 cur 
        cur += arr[idx]
        # cur이 양수면 max가 될수 있는 후보이므로 리스트에 추가
        if cur > 0:
            candidate.append(cur)
        # cur이 음수면 무조건 max(arr)보다 작으므로 0으로 초기화
        if cur < 0:
            cur = 0
        # idx 증가
        idx += 1
    # arr의 최대값과 연속합의 후보들의 값 비교
    print(max(max(candidate), max(arr)))
# case2 모두 양수일때
elif min(arr) > 0:
    print(sum(arr))
# case3 모두 음수 혹은 0일때
elif max(arr) <= 0:
    print(max(arr))

