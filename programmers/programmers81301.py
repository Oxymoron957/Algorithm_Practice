"""
숫자 문자열과 영단어

https://programmers.co.kr/learn/courses/30/lessons/81301
"""


def solution(s):
    returnSring = []
    index = 0
    c = s[index]
    while True:
        # if c is number
        if c.isnumeric():
            returnSring.append(c)
            index += 1
        # if c is string 
        else:
            numStr = ''
            if c== 'z':
                returnSring.append('0')
                numStr = 'zero'
            elif c == 'o':
                returnSring.append('1')
                numStr = 'one'
            elif c == 't' and s[index+1] == 'w':
                returnSring.append('2')
                numStr = 'two'
            elif c == 't' and s[index+1] == 'h':
                returnSring.append('3')
                numStr = 'three'
            elif c == 'f' and s[index+1] == 'o':
                returnSring.append('4')
                numStr = 'four'
            elif c == 'f' and s[index+1] == 'i':
                returnSring.append('5')
                numStr = 'five'
            elif c == 's' and s[index+1] == 'i':
                returnSring.append('6')
                numStr = 'six'
            elif c == 's' and s[index+1] == 'e':
                returnSring.append('7')
                numStr = 'seven'
            elif c == 'e':
                returnSring.append('8')
                numStr = 'eight'
            elif c == 'n':
                returnSring.append('9')
                numStr = 'nine'
            
            index += len(numStr)

        if index == len(s):
            break
        else:
            c = s[index]
    
    return int(''.join(returnSring))



        



print(solution('threethreethreethreethreethreethreethreethreethreethreethreethreethreethreethreethreethreethreethreethreethree'))


