# -*- coding: utf-8 -*-
"""
주사위 쌓기
https://www.acmicpc.net/problem/2116
"""

"""
여러가지 주사위를 쌓는다
- 서로 붙어있는 주사위 면의 숫자는 같아야한다. 
- 쌓아올린 사각 기둥의 한 면의 숫자합이 최대가 되도록 

-> 하나의 숫자를 골랐을 때 반대편에 어떤 숫자가 정해지는지 알아야한다.
0 -> 5
1 -> 3
2 -> 4

-> 주사위의 순서는 같아야한다.
	- 가장 아래 주사위의 의해 다른 주사위의 옆 숫자가 결정된다.

-> 합의 최대를 구한다.
"""

N = int(input())
dice = []
for _ in range(N):
	dice.append(list(map(int, input().split())))

cases = {0:5, 1:3, 2:4, 5:0, 3:1, 4:2}

answer = 0
# 가장 아래 주사위에 의해 나머지 주사위의 경우가 정해지므로, 가장 아래 주사위의 모든 경우의 수 대입
for i in range(6): 
	dice_max = [] # 각 주사위의 옆면의 최대값
	dice_number = [1, 2, 3, 4, 5, 6]

	# 가장 아래 주사위의 아래&위 숫자 결정
	dice_number.remove(dice[0][i]) 
	next_number = dice[0][cases[i]]
	dice_number.remove(next_number)
	
	# 가장 아래 주사위의 옆면들 중 가장 큰 값 삽입
	dice_max.append(max(dice_number)) 

	# 다른 주사위에 대해서
	for j in range(1, N): 
		dice_number = [1, 2, 3, 4, 5, 6]
		
		# 이전 주사위의 정보를 통해 윗면의 숫자 및 옆면의 숫자를 도출한다.
		dice_number.remove(next_number) 
		next_number = dice[j][cases[dice[j].index(next_number)]] 
		dice_number.remove(next_number)
		
		# 가장 아래 주사위의 옆면들 중 가장 큰 값 삽입
		dice_max.append(max(dice_number)) 
	
	# 최댓값 도출 
	if answer < sum(dice_max):
		answer = sum(dice_max)

print(answer)
