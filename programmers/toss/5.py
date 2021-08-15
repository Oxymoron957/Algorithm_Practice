"""
과일 게임
"""

def solution(fruitWeights, k):
    weights = set()
    for idx in range(0, len(fruitWeights)-k+1):
        # weights.add(max(fruitWeights[idx:idx+k]))
        first = fruitWeights
    return sorted(list(weights), reverse=True)


print(solution([30, 40, 10, 20, 30], 3))