# -*- coding: utf-8 -*-
"""
전화번호 목록
https://programmers.co.kr/learn/courses/30/lessons/42577
"""

def solution(phone_book):
    hash_map = {}
    for i in phone_book:
        hash_map[i] = 1
    for i in phone_book:
        temp_string = ""
        for j in i:
            temp_string += j
            # print(temp_string, i)
            if temp_string in hash_map and temp_string != i:
                return False
            if len(i) < len(temp_string):
                break
    return True
    

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
