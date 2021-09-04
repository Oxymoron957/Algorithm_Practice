"""
조이스틱
https://programmers.co.kr/learn/courses/30/lessons/42860

*몰랐던 점
ord('A') : 해당 charactor의 ascii 값을 반환한다.
"""

def solution(name):
    # variables
    listChar = list(name)
    ch = listChar[0]
    curIdx = 0
    move = 0

    while True:
        # 해당 알파벳을 맞추는 작업 (A부터 정방향으로 갔을때의 cost / 역방향으로 갔을때의 cost)
        move += min(ord(ch)-ord('A'), abs(ord(ch)-ord('Z'))+1)
        listChar[curIdx] = 'Checked'

        # 어디를 가는 것이 효율적인지 계산 => 방문한 곳이 아니며 A가 아니고 가장 low cost로 갈 수 있는 곳 (가까이 있는 곳)
        nextCost = [min(abs(x-curIdx), len(listChar)-abs(x-curIdx)) if listChar[x] != 'Checked' and listChar[x] != 'A' else 2**32 for x in range(len(listChar))]
        
        # 모든 element를 바꾸었을때 종료
        if min(nextCost) == 2**32:
            break

        # 다음 index로 이동
        move += min(nextCost)
        curIdx = nextCost.index(min(nextCost))
        ch = listChar[curIdx] 

    return move
        

print(solution('JAZ'))
print(solution('JEROEN'))
print(solution('AAABAAAAAB'))

