"""
110 옮기기
https://programmers.co.kr/learn/courses/30/lessons/77886

1. 문자열에서 110을 모두 제거해야한다
2. 제거한 110을 적절한 위치에 삽입한다.
"""

def solution(s):
    answer = []
    for inputStr in s:
        # Stack을 이용해서 inputStr의 생기는 모든 110을 제거한다. 
        count110 = 0
        stack = []
        for c in inputStr:
            if c == '0' and len(stack) >= 2 and stack[-2:] == ['1','1']:
                stack.pop()
                stack.pop()
                count110+=1
            else:
                stack.append(c)
        # 가장 뒤에 있는 0 위치에 삽입 or 0이 없다면 1 앞에 삽입
        # print(stack)
        isZeroExist = False
        for i in range(len(stack)-1, -1, -1):
            if stack[i] == '0':
                answer.append(''.join(stack[:i+1] + ['1','1','0']*count110 + stack[i+1:]))
                isZeroExist = True
                break
        if not isZeroExist: 
            answer.append(''.join(['1','1','0']*count110 + stack))
        
    return answer

# def solution(s):
#     answer = []
#     for inputStr in s:
#         while True:
#             isChanged = False
#             if '1100' in inputStr:
#                 index1100 = inputStr.index('1100')
#                 inputStr = inputStr[:index1100] + '0110' + inputStr[index1100+4:]
#                 isChanged = True
#             if '1110' in inputStr:
#                 index1110 = inputStr.index('1110')
#                 inputStr = inputStr[:index1110] + '1101' + inputStr[index1110+4:]
#                 isChanged = True
#             if not isChanged:
#                 answer.append(inputStr)
#                 break
#     return answer


print(solution(["000", "1110","100111100","0111111010"]))
    