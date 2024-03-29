"""
문제 설명
정수 1, 2, 3을 담고 있는 배열이 주어집니다. 이 배열에 원소를 추가해서 배열 안의 1, 2, 3의 개수가 모두 같아지도록 하려 합니다. 단, 추가하는 원소의 개수는 최소가 되어야 합니다.

다음은 입출력 예제 1번의 배열을 나타낸 예시입니다.

[2, 1, 3, 1, 2, 1]
위 배열에 원소 2, 3, 3을 순서대로 추가하면 다음과 같이 바뀝니다.

[2, 1, 3, 1, 2, 1, 2, 3, 3]
원소 1, 2, 3의 개수가 모두 3개로 같아졌습니다. 세 개보다 적은 개수의 원소를 추가하여 1, 2, 3의 개수가 같도록 만드는 방법은 없으며, 추가해야 하는 원소는 1: 0개, 2: 1개, 3: 2개입니다.

정수 1, 2, 3을 담고 있는 배열 arr가 매개변수로 주어집니다. 원소 추가를 최소로 하여 배열 안의 1, 2, 3 각각의 개수가 모두 같도록 만들 때, 추가해야 하는 각 원소의 개수를 1, 2, 3 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.
"""
def solution(arr):
    num_1 = arr.count(1)
    num_2 = arr.count(2)
    num_3 = arr.count(3)
    max_ = max(num_1, num_2, num_3)
    more_1 = max_ - num_1
    more_2 = max_ - num_2
    more_3 = max_ - num_3

    answer = [more_1, more_2, more_3]
    return answer


print(solution([1, 2, 3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]))
