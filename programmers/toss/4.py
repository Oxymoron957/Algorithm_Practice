"""
유용한 금융 정보
"""

def solution(input):
    inputs = input.split('\n')
    curState = True
    answer = []
    answer.append(inputs[0])
    showCount = 0
    showDay = int(inputs[0].split()[0])+1
    for i in inputs[1:]:
        if i == 'SHOW':
            if curState == True:
                # 1 추가
                answer.append('\n1')
                showCount += 1
            elif showCount >= int(inputs[0].split()[1]):
                # 0 추가
                answer.append('\n0')
        elif i == 'NEXT':
            answer.append('\n-')
            showDay -= 1
        elif i == 'EXIT':
            answer.append('\nBYE')
        else:
            answer.append('\nERROR')

        if showDay == 0:
            showDay = int(inputs[0].split()[0])+1   
            showCount = 0
    return ''.join(answer)

print(solution("1 2\nSHOW\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nEXIT"))
