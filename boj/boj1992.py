"""
쿼드트리
https://www.acmicpc.net/problem/1992
"""

# variables
N = int(input())
map_ = []
answer = ''
for i in range(N):
    map_.append(list(input()))

# check if all elements are 0s or 1s
def checkSet(map_):
    checkSet = set()
    for rows in map_:
        for elements in rows:
            checkSet.add(elements)
    if list(checkSet) == ['0']:
        return '0'
    elif list(checkSet) == ['1']:
        return '1'
    else:
        return False

# recursive function
def quadTree(map_, size_):
    global answer

    # divide 
    firstSector = [x[0:int(size_/2)] for x in map_[0: int(size_/2)]]
    secondSector = [x[int(size_/2): size_] for x in map_[0: int(size_/2)]]
    thirdSector = [x[0: int(size_/2)] for x in map_[int(size_/2):size_]]
    forthSector = [x[int(size_/2):size_] for x in map_[int(size_/2):size_]]

    # check 
    for sector in [firstSector, secondSector, thirdSector, forthSector]:
        element = set()
        for e in sector:
            for nums in e:
                element.add(nums)
        if len(element) != 1:
            answer += '('
            quadTree(sector, len(sector))
            answer += ')'
        elif list(element) == ['1']:
            answer += '1'
        elif list(element) == ['0']:
            answer += '0'
    
isPure = checkSet(map_)
if isPure:
    print(isPure)
else:
    quadTree(map_, N)
    print('('+answer+')')

