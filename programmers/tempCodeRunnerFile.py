		# print(dq)
		val, level, li = dq.popleft()
		if level == len(numbers) and val == target:
			# print(li)
			answer += 1
		if level < len(numbers):
			dq.append([val+numbers[level], level+1, li + [numbers[level]]])
			dq.append([val-numbers[level], level+1, li + [-1*numbers[level]]])
	return answer
