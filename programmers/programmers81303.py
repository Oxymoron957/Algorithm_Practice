"""
표 편집
https://programmers.co.kr/learn/courses/30/lessons/81303
"""

from collections import deque

def solution(n, k, cmd):
    li = [ x*10 for x in range(n)]

    sel = [k, li[k]]
    stack_ = deque()
    print(li, sel)
    for c in cmd:
        if c[0] == 'U':
            print("Select Upper Row")
            sel[0] -= int(c[2])
            sel[1] = li[sel[0]]
            print(li, sel)

        elif c[0] == "D":
            print("Select Down Row")
            sel[0] += int(c[2])
            sel[1] = li[sel[0]]
            print(li, sel)

        elif c[0] == "C":
            print("Delete Current Row")
            stack_.append(sel[1])
            li.remove(li[sel[0]])

            if len(li)-1 == sel[0]:
                sel[0] -= 1
                sel[1] = li[sel[0]]
            else:
                sel[1] = li[sel[0]]
            print(li, sel, stack_)

        elif c[0] == "Z":
            print("Restore last deletion")
            li.append(stack_.pop())
            li.sort()
            print(li, sel, stack_)

    answer = ''
    for i in range(n):
        if i*10 not in li:
            answer += 'X'
        else:
            answer += 'O'
    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
