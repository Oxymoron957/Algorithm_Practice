"""
문제 설명
해외 여행을 매우 좋아하는 준이 다니고 있는 대표적인 푸드테크 기업 W는 주 35시간 근무, 시간제 휴가로 유명한 회사입니다. 준은 회사의 출퇴근 시간을 잘 활용하여 해외 여행은 항상 금요일에 출발하여 다음 월요일에 돌아오도록 여행 일정을 세웁니다.

요일	출근 시간	퇴근 시간
월	1PM	6PM
금	9:30AM	6PM
올해 호치민을 마지막으로 다녀온 준은 남은 휴가 시간을 고려하지 않은 채 비행기 시간만 고려하여 여행 일정을 세웠습니다. 올해 남은 휴가 시간 time과 여행 일정을 담은 이차원 배열 plans가 매개변수로 주어질 때, 남은 휴가 시간 내에 갈 수 있는 여행지 중 준의 올해 마지막 여행지가 어디인지 return 하도록 solution 메서드를 완성해주세요.
"""

def solution(time, plans):
    time2spend = 0
    trip_name = plans[0][0]
    for trip in plans:
        name, start, end = trip

        startTime, startAM_PM = int(start[:-2]), start[-2:]
        # print(startTime, startAM_PM)
        # 금요일 오전에 출발할 때
        if startAM_PM == 'AM':
            # 출근시간 이전일 때
            if startTime < 9.5:
                time2spend += 8.5
            # 출근 시간 이후일 때
            if startTime > 9.5:
                time2spend += (6 + (12 - startTime))
        # 금요일 오후에 출발할 때
        if startAM_PM == 'PM':
            # 퇴근시간 이전일때
            if startTime < 6:
                time2spend += 6 - startTime
            # 퇴근시간 이후일때 -> OK
            if startTime >= 6:
                pass

        endTime, endAM_PM = int(end[:-2]), end[-2:]
        # print(endTime, endAM_PM)
        # 월요일 오전에 도착할 때 -> OK
        if endAM_PM == 'AM':
            pass
        # 월요일 오후에 도착할 때
        if endAM_PM == 'PM':
            # 출근 시간 이전일때 -> OK
            if endTime < 1:
                pass
            # 퇴근 시간 이전일 때
            if 1 < endTime < 6:
                time2spend += (endTime - 1)
            # 퇴근 시간 이후일 때:
            if endTime >= 6:
                time2spend += 5

        if time2spend <= time:
            trip_name = name
        else:
            break

    return trip_name


    # answer = ''
    # return answer

# print(solution(3.5, [ ["홍콩", "10AM", "9AM"]]))
print(solution(4, [ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"], ["호주", "11PM", "9AM"]]))
