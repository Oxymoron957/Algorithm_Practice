def solution(people, limit):
    people = sorted(people)
    numOfBoat = 0
    left = 0
    right = len(people)-1
    while left <= right:
        print(left, right, numOfBoat)
        if people[left]+people[right] > limit:
            numOfBoat+=1
            right -= 1
        else:
            left+=1
            right-=1
            numOfBoat+=1
    return numOfBoat




print(solution([70,50, 80], 100))

