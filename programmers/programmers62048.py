import math

def solution(w,h):
    gcd = math.gcd(w, h)

    if gcd == 1:
        return w*h-(w+h-1)
    else:
        local_w = int(w/gcd)
        local_h = int(h/gcd)
        return w*h - (local_w+local_h-1)*gcd

    
        

print(solution(100000000, 100000000))

