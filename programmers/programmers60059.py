"""
자물쇠와 열쇠
https://programmers.co.kr/learn/courses/30/lessons/60059
"""
import copy

def unlock(this_map, lock_size):
    for i in this_map:
        print(i)
    print()
    for i in range(lock_size-1, lock_size-1+lock_size):
        for j in range(lock_size-1, lock_size-1+lock_size):
            if this_map[i][j] != 1:
                return False
    return True

def rotation(key):
    key_rot = [copy.deepcopy(key)]
    temp = copy.deepcopy(key)
    for i in range(3):
        rotated = [[0]*len(key) for _ in range(len(key))]
        for j in range(len(key)):
            for k in range(len(key)):
                rotated[j][k] = temp[k][len(key)-j-1]
        key_rot.append(rotated)

        temp = copy.deepcopy(rotated)
    return key_rot



def solution(key, lock):
    map_size = len(lock)+ (len(lock)-1)*2
    lock_size = len(lock)
    key_size = len(key)
    this_map = [[0]*map_size for _ in range(map_size)]
    for i in range(lock_size-1, lock_size-1+lock_size):
        for j in range(lock_size-1, lock_size-1+lock_size):
            this_map[i][j] = lock[i-lock_size+1][j-lock_size+1]
    
    keys = rotation(key)

    accessable = False
    for akey in keys:
        for i in range(map_size-key_size+1):
            for j in range(map_size-key_size+1):
                new_map = copy.deepcopy(this_map)
                for k in range(key_size):
                    for t in range(key_size):
                        new_map[i+k][j+t] += akey[k][t]
                if unlock(new_map, lock_size):
                    return True
    if not accessable:
        return False
        

print(solution([[1, 0, 1], [0, 0, 0], [1, 0, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
