"""
매출 하락 최소화
https://programmers.co.kr/learn/courses/30/lessons/72416
"""

def solution(sales, links):
    motherNode = sorted([x[0] for x in links])
    childNode = sorted([x[1] for x in links])

    links.sort(key = lambda x : x[0])
    
    for i in range(1,11):
        motherNodeGroup = list(filter(lambda x:x[0]==i, links))
        minValue = 2**32
        for j in [x[1] for x in motherNodeGroup]:
            childNodeGroup = [x[1] for x in list(filter(lambda x:x[0]==j, links))]
            print(childNodeGroup)
            
print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))

