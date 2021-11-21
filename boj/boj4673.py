"""
셀프 넘버
https://www.acmicpc.net/problem/4673

몰랐던 점 :
중복된 요소를 피할 때는 set() 자료구조 사용하자!
"""

nums = set(range(1, 10001))
generated_nums = set()

for i in range(1, 10000):
    generated_nums.add(i + sum(list(map(int, list(str(i))))))

self_nums = sorted(nums - generated_nums)
for i in self_nums:
    print(i)