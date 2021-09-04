"""
큰 수 만들기
https://programmers.co.kr/learn/courses/30/lessons/42883

몰랐던 점 :
처음엔 순열 혹은 정렬을 통해 풀려고 했으나 숫자의 순서가 바뀌지 않아야해서 구현이 어려웠다.
오히려 숫자의 순서가 바뀌면 안된다는 점에서 stack 자료구조를 생각했어야 하는데 아쉽다. 
"""


def solution(number, k):
    stack = []
    for n in number:
        # print(n)
        if not stack:
            stack.append(n)
            continue
        if k > 0:
            while stack and int(stack[-1]) < int(n):
                stack.pop()
                k-= 1
                if not stack or k <= 0:
                    break
        stack.append(n)
    
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)


#이전 코드 
"""
def solution(number, k):
    # numList = list(map(int,list(number)))
    # numListIdx = [[x,numList.index(x)] for x in numList ]
    # print(numList)
    # print(numListIdx)
    # numListIdxSorted = sorted(numListIdx, key=lambda x:(x[0], x[1]))

    lenNum = len(number)
    numList = list(map(int,list(number)))
    numListSorted = sorted(numList, reverse= True)
    print(numList, numListSorted)
    for i in numListSorted:
        if not(len(numList) - numList.index(i) < k):
            numList = numList[numList.index(i):]
            break
    numListSorted = sorted(numList, reverse= True)
    print(numList, numListSorted)
    while len(numList) != lenNum- k:
        numList.remove(numListSorted.pop())
    print(numList)
"""

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))