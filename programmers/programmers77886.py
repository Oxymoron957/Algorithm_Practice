"""
110 옮기기
https://programmers.co.kr/learn/courses/30/lessons/77886
"""

def solution(s):
    answer = []

    for inputStr in s:
        while True:
            print(inputStr)
            changed = False
            if '110' in inputStr and '111' in inputStr:
                index110 = inputStr.rfind('110')
                if index110-1 < len(inputStr) and inputStr[index110-1] == 1:
                     inputStr[index110+1] = 0
                     inputStr[index110+2] = 1
                # index110 = inputStr.rfind('110')
                # index111 = inputStr.index('111')
                # if index110 > index111:
                #     # inputStr = list(inputStr)
                #     # inputStr[index110] = '1'
                #     # inputStr[index111] = '0'
                #     # inputStr = ''.join(inputStr)
                    
                #     changed = True
            if not changed:
                answer.append(inputStr)
                break
    return answer



print(solution(["1110","100111100","0111111010"]))
    