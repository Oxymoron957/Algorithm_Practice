"""
주식가격
https://programmers.co.kr/learn/courses/30/lessons/42584

※ enumerate 생각보다 시간소모가 많이 된다. range()만 쓰는게 좋을것 같다. 
"""

def solution(prices):
    answer = []
    for idx1 in range(len(prices)):
        time = 0
        for idx2 in range(idx1+1, len(prices)):
            time += 1
            if prices[idx1] > prices[idx2]:
                break
        answer.append(time)
        
    return answer

print(solution([1, 2, 3, 2, 3]))



