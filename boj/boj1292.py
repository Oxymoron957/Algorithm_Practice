start, end = [int(x) for x in input().split()]

num_list = []

i=1

while len(num_list)<end:
    num_list.extend([i]*i)
    i+=1

print(num_list[start-1:end])
print(sum(num_list[start-1:end]))