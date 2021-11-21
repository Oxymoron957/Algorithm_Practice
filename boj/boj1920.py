"""
수 찾기
https://www.acmicpc.net/problem/1920

몰랐던 점:
input()보다 sys.stdin.readline()를 쓰자
"""

import sys

N = int(input())
A_array = list(map(int, sys.stdin.readline().split()))
M = int(input())
M_array = list(map(int, sys.stdin.readline().split()))

for i in M_array:
    if i in A_array:
        print(1)
    else:
        print(0)
