"""
오큰수 20210810
https://www.acmicpc.net/problem/17298


※ 부족했던 부분
어떤 조건이 걸렸을 때 스택에 있는 원소를 검사하며 스택을 비우는 기능 
이 문제의 경우엔 바로 옆의 수가 오큰수가 아닐 경우 스택에 넣고 바로 옆의 수가 오큰수인 조건에 스택에 존재하는 원소들도 오큰수를 가지는지 조사한다.   
"""

from collections import deque
import sys

# input 
SIZE = int(sys.stdin.readline())
NUM_ARR= list(map(int, sys.stdin.readline().split()))

# make variables (deque)
answer = [-1 for _ in range(SIZE)]
st = deque()
st.append(0)
cur_idx = 1


while st and cur_idx <= SIZE-1:
    while st and NUM_ARR[st[-1]] < NUM_ARR[cur_idx]:
        answer[st.pop()] = NUM_ARR[cur_idx]
   
    st.append(cur_idx)
    cur_idx+=1
    
for i in answer:
    print(i, end=' ')


    
