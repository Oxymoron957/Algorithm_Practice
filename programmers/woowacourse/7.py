"""


"""

from collections import deque

def solution(grid, clockwise):
    gridComponent = [[] for x in range(len(grid))]

    if clockwise == True:
        for i,v in enumerate(grid[::-1]):
            component = deque(v)
            
            gridComponent[i].append(component.popleft())
            
            idx = i+1
            while component:
                a = component.popleft()
                b = component.popleft()
                gridComponent[idx].append(b)
                gridComponent[idx].append(a)
                idx += 1
    else:
        for i,v in enumerate(grid[::-1]):
            component = deque(v)
            
            gridComponent[i].append(component.pop())
            
            idx = i+1
            while component:
                a = component.pop()
                b = component.pop()
                gridComponent[idx].append(b)
                gridComponent[idx].append(a)
                idx += 1
        for i in range(len(gridComponent)):
            gridComponent[i] = gridComponent[i][::-1]

    answer = []
    for i in gridComponent:
        answer.append(''.join(i))
    return answer

# print(solution(["1","234","56789"], True)) 
# print(solution(["A","MAN","DRINK","WATER11"], True)) 
print(solution(["A","MAN","DRINK","WATER11"], False))
