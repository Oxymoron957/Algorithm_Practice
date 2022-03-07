# -*- coding: utf-8 -*-
"""
가장 큰 수
https://programmers.co.kr/learn/courses/30/lessons/42746
"""

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda x:x*3)
    return str(int("".join(numbers)))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
# print(solution([8, 890, 85]))


# def solution(numbers):
#     nums = []
#     for i in numbers:
#         nums.append([i])
    
#     max_10s = len(str(max(numbers)))
#     print(max_10s)    
    
#     for i, x in enumerate(map(str, numbers)):
#         w = 0
#         cur_w = 1000
#         for j in x:
#             w += int(j) * cur_w
#             cur_w /= 10
#             w -= len(x)
#         nums[i].append(w)
        
    
#     nums.sort(key=lambda x: x[1], reverse=True)
#     print(nums)
#     answer = ''
#     for i in nums:
#         answer += str(i[0])
#     return answer
