"""
전화번호 목록
https://programmers.co.kr/learn/courses/30/lessons/42577

몰랐던 점 :
단순 비교 문제지만, 정렬을 먼저 해놓음으로써 시간복잡도를 ^2에서 nlogn으로 줄일 수 있다.
(비슷한(접두어)는 정렬해도 비슷한 위치에 놓인다)
"""


def solution(phone_book):
    size = len(phone_book)
    phone_book.sort()

    # 원래 코드
    # for i in range(size):
    #     for j in range(i+1, size):
    #         # print(phone_book[i], phone_book[j])
    #         short_num, long_num = (phone_book[i], phone_book[j]) if len(phone_book[i]) < len(phone_book[j]) else (phone_book[j], phone_book[i])
    #         # print(short_num, long_num)
    #         if short_num == long_num[:len(short_num)]:
    #             return False

    for i in range(size-1):
        short_num, long_num = (phone_book[i], phone_book[i+1]) if len(phone_book[i]) < len(phone_book[i+1]) else (phone_book[i+1], phone_book[i])
        if short_num == long_num[:len(short_num)]:
                return False
    return True



print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
