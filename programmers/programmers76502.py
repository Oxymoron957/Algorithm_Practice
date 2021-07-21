"""
괄호 회전하기
https://programmers.co.kr/learn/courses/30/lessons/76502
"""


def solution(s):
    s_list = list(s)
    count = 0
    for _ in range(len(s_list)):
        # modify
        s_list.append(s_list.pop(0))
        # init stack
        stack = []
        # init check 
        check = True
        for c in s_list:
            # check whether this is correct string
            if stack and c == ']':
                if stack.pop() != '[':
                    check = False
                    continue
            elif stack and c == ')':
                if stack.pop() != '(':
                    check = False
                    continue
            elif stack and c == '}':
                if stack.pop() != '{':
                    check = False
                    continue
            else:
                stack.append(c)
        # if stack is not empty, not a correct string
        if stack:
            pass
        # if stack is empty, it's a correct string
        elif check:
            count += 1
    return count
                
print(solution("}}}"))
