"""
입실 퇴실
https://programmers.co.kr/learn/courses/30/lessons/86048
"""

def solution(enter, leave):
    # variables
    room = [] # 사람들이 있는 방 
    count = {} # 만난 사람들 저장하는 dictionary
    for person in sorted(enter):
        count[person] = set()

    # 모두 나갈 때까지 loop
    while leave:
        # leave에서 나갈 사람이 room에 들어올 때까지 room에 사람 입장
        exitperson = leave.pop(0)
        if not enter:
            break
        while enter and enter[0] != exitperson:
            room.append(enter.pop(0))
        if enter:
            room.append(enter.pop(0))
        
        # room에 들어온 사람들은 서로 만날 수밖에 없으므로 dictionary에 정보 추가 
        for person in room:
            for other in [x for x in room if x!=person]:
                count[person].add(other)

        # room에서 나갈 사람 나가기 
        room.remove(exitperson)
        while leave and leave[0] in room:
            room.remove(leave.pop(0))
    
    return [len(x) for x in list(count.values())]   
    

print(solution([1,3,2], [1,2,3]))
print(solution([1,4,2,3], [2,1,3,4]))
print(solution([3,2,1], [2,1,3]))
print(solution([3,2,1], [1,3,2]))
print(solution([1,4,2,3], [2,1,4,3]))
