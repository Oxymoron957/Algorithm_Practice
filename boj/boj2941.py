"""
크로아티아 알파벳
https://www.acmicpc.net/problem/2941

몰랐던 점 :
string replace 함수 : (바꿀문자열, 바뀐문자열, *바꿀횟수*) 
"""

input_str = input()

# print(input_str)

croatia_count = 0

def croatia_search(alphabet):
    global input_str, croatia_count
    if alphabet in input_str:
        input_str = input_str.replace(alphabet, ' ', 1)
        croatia_count += 1
        # print(input_str)
        return True
    return False

while croatia_search('c='):
    pass
while croatia_search('c-'):
    pass
while croatia_search('dz='):
    pass
while croatia_search('d-'):
    pass
while croatia_search('lj'):
    pass
while croatia_search('nj'):
    pass
while croatia_search('s='):
    pass
while croatia_search('z='):
    pass


print(croatia_count + len(input_str.replace(' ', '')))