"""
스위치 켜고 끄기
https://www.acmicpc.net/problem/1244
"""

import sys

num_switch = int(sys.stdin.readline())
switch_stat = list(map(int, sys.stdin.readline().split()))
students = int(sys.stdin.readline())
for _ in range(students):
	student, number = list(map(int, sys.stdin.readline().split()))
	
	if student == 1:
		cur_n = number
		while cur_n < num_switch:
			switch_stat[cur_n-1] = 1 if switch_stat[cur_n-1] == 0 else 0
			cur_n += number
	if student == 2:
		scope = 1
		switch_stat[number-1] = 1 if switch_stat[number-1] == 0 else 0
		while number-scope-1 >= 0 and number+scope-1 <= len(switch_stat) and (switch_stat[number+scope-1] == switch_stat[number-scope-1]):
			switch_stat[number+scope-1] = 1 if switch_stat[number+scope-1] == 0 else 0
			switch_stat[number-scope-1] = 1 if switch_stat[number-scope-1] == 0 else 0
			scope += 1
print(" ".join(map(str, switch_stat)))
