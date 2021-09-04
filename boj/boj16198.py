"""
에너지 모으기
https://www.acmicpc.net/problem/16198
"""

N = int(input())
numList = list(map(int, input().split()))
answerList = []

def iterFunc(numList, N, answer):
    global answerList

    if N == 2:
        answerList.append(answer)
    else:
        for i in range(1, N-1):
            iterFunc(numList[:i]+numList[i+1:], N-1, answer+numList[i-1]*numList[i+1])

iterFunc(numList, N, 0)
# print(answerList)
print(max(answerList))
