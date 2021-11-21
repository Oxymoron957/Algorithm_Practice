"""
금과 은 운반하기
https://programmers.co.kr/learn/courses/30/lessons/86053

**다시풀기
"""

def solution(a, b, g, s, w, t):
    start = 0 # 시작시간
    end = (10 ** 9) * (10 ** 5) * 4 # 끝나는 시간
    answer = (10 ** 9) * (10 ** 5) * 4 # 제일 짧은 시간

    while start <= end: 
        # 이분탐색 시작
        mid = (start + end) // 2
        # 현재 금, 은 
        current_gold = 0
        current_silver = 0
        total = 0

        # 도시 idx & 도시 소요 시간 
        for i, time in enumerate(t):
            # move count 계산
            cnt = (mid - time) // (time * 2) + 1
            # 해당 도시의 최대 gold 이동량 계산 
            if cnt * w[i] > g[i]:
                current_gold += g[i]
            else:
                current_gold += cnt * w[i]
            # 해당 도시의 최대 silver 이동량 계산
            if cnt * w[i] > s[i]:
                current_silver += s[i]
            else:
                current_silver += cnt * w[i]
            # 해당 도시의 최대 이동량 계산
            if s[i] + g[i] < cnt * w[i]:
                total += s[i] + g[i]
            else:
                total += cnt * w[i]

        if current_gold >= a and current_silver >= b and total >= a + b:
            # 조건이 충족된다면 answer, end 갱신
            end = mid - 1
            answer = min(answer, mid)
        else:
            # 아닐경우 start 갱신
            start = mid + 1

    return answer

print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))
