"""
멀쩡한 사각형
https://programmers.co.kr/learn/courses/30/lessons/62048
"""

from math import gcd

def solution(w,h):
    gcd_ = gcd(w, h)
    # print(gcd_)
    if w == 1 or h == 1:
        return 0
    
    if gcd_ == 1:
        print(w*h, min(w,h))
        return w*h - (min(w,h)*2)
    elif gcd_ == w == h:
        return w*h - w
    else:
        # print(w*h , max(w,h), gcd_)
        return w*h - gcd_*gcd_


print(solution(8, 12))
print(solution(4, 4))
print(solution(3, 3))
print(solution(12, 8))
print(solution(3, 1))






















"""
import math

def solution(w,h):
    gcd = math.gcd(w, h)

    if gcd == 1:
        return w*h-(w+h-1)
    else:
        local_w = int(w/gcd)
        local_h = int(h/gcd)
        return w*h - (local_w+local_h-1)*gcd
"""
    
        


