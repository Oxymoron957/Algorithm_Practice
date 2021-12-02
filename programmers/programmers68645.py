"""
삼각 달팽이
https://programmers.co.kr/learn/courses/30/lessons/68645
"""

def move_down(answer, start_num, cur_n, cur_level, cur_circle):
    # print("down", answer, start_num, cur_n, cur_level)
    idx = 0
    for i in range(start_num, start_num+cur_n):
        # print(cur_level + i)
        answer[cur_level + idx-1].insert(cur_circle-1,i)

        idx+=1

def move_up(answer, start_num, cur_n, cur_level, cur_circle):
    idx = 0
    # print("up", answer, start_num, cur_n, cur_level)
    for i in range(start_num, start_num+cur_n):
        # print(cur_level - idx-1)
        answer[cur_level - idx-1].insert(cur_circle,i)
        idx += 1

    
def move_horizontal(answer, start_num, cur_n, cur_level, cur_circle):
    idx = 0
    # print("hori", answer, start_num, cur_n, cur_level)
    for i in range(start_num, start_num+cur_n):
        # print(cur_level + i)
        # print(cur_level -1)
        answer[cur_level-1].insert(cur_circle+1,i)
        # answer[cur_level-1].append(i)
        idx += 1

def solution(n):
    answer = [[] for x in range(n)]
    # print(answer)
    start_num = 1
    cur_level = 1
    cur_circle = 1
    
    while n > 0:    
        
        move_down(answer, start_num, n, cur_level, cur_circle)
        start_num += n
        n -= 1
        cur_level += n
        
        move_horizontal(answer, start_num, n, cur_level, cur_circle)
        start_num += n
        n -= 1
        cur_level -= 1
        
        move_up(answer, start_num, n, cur_level, cur_circle)
        start_num += n
        n -= 1
        cur_level -= (n-1)

        cur_circle += 1

    return_arr = []
    for i in answer:
        return_arr += i
    # return return_arr
    return answer
 
print(solution(4))
print(solution(5))
print(solution(6))

