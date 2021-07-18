"""
파일 합치기
https://www.acmicpc.net/problem/11066
"""

"""
합치는 파일이 연속적이어여야 된다!
1
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32

"""

T = int(input())

for _ in range(T):
    cost = 0
    K = int(input())
    num_arr = list(map(int, input().split()))
    num_arr.sort()
    print(num_arr)
    index = 0
    while True:
        if index+2 >= len(num_arr): 
            index = 0
        if num_arr[index]+num_arr[index+1] > num_arr[index+2]:
            cost += num_arr[index]+num_arr[index+1]
            num_arr[index:index+2] = [num_arr[index]+num_arr[index+1]]
            index += 1
        else:
            index = 0


        if len(num_arr) <= 3:
            cost += sum(num_arr)
            print(cost)

        
        print(num_arr, index)
        K-=1

