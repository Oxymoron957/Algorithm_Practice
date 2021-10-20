"""
영어 끝말잇기
https://programmers.co.kr/learn/courses/30/lessons/12981
"""

def solution(n, words):
    spoken = dict()
    turns = dict()
    turns[1] = 1
    pairs = []
    turn = 2
    for i in range(len(words)-1):
        pairs.append([words[i], words[i+1]])
    pairs.append([words[-1], words[0]])
    
    length = 0
    for a, b in pairs:
    
        # print(length, turn, a, b)
        if length == len(pairs)-1:
            return [0, 0]

        if a[-1] != b[0]:
            # print(a, b)
            return [turn, turns[turn]]
        
        if spoken.get(b) != None:
            return [turn, turns[turn]]

        if spoken.get(a) == None:
            spoken[a] = 1
        else:
            spoken[a] += 1
        
        turn = (turn+1)%(n+1)
        if turn == 0:
            turn = 1
        if turns.get(turn) == None:
            turns[turn] = 1
        else:
            turns[turn] += 1
        length += 1
    return [0, 0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

