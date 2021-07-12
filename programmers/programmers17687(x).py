"""
n 진수 게임
https://programmers.co.kr/learn/courses/30/lessons/17687

"""

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):
    cur_num = 0
    answer_array = []
    return_array = []
    turn = 1
    cur_time = 0
    while True:
        # n진법으로 변환 
        answer = convert(cur_num, n)

        # 변환한 수를 배열에 삽입
        if len(answer) > 1:
            for c in answer:
                answer_array.append(c)
        else:
            answer_array.append(answer)
        cur_num+=1

        # 몇번째 정답이 필요한지 계산 m의 p번째 
        turn = (turn+1)%m
        print(turn)
        print(answer_array)
        if turn == p-1:
            #print(turn)
            
            return_array.append(answer_array[-1])
            cur_time += 1
        # 답 반환 
        if cur_time == t:
            print(return_array)
            break


solution(2, 4, 2, 1)