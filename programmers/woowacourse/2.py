"""
문제 설명
당신은 스마트폰 어플리케이션을 이용하여 공부한 시간을 기록하려합니다. 어플리케이션의 기능은 다음과 같습니다.

시작 버튼: 공부를 시작할 때의 시각을 기록합니다.
중지 버튼: 공부를 중지할 때의 시각을 기록합니다.
하지만, 어플리케이션에 기록된 시간에 항상 공부만 했다는 보장이 없기 때문에 다음과 같은 규칙을 적용해 실제로 공부한 시간을 구하려 합니다.

공부를 시작하고 5분이 지나기 전에 중지했다면 실제로 공부한 시간에 포함시키지 않습니다.
공부를 시작하고 1시간 45분이 넘어서 중지했다면 1시간 45분까지만 공부한 시간으로 인정합니다.
공부를 시작한 시각과 중지한 시각이 연속적으로 주어집니다. 처음 주어진 시각은 무조건 공부를 시작한 시각이며, 마지막 시각은 무조건 공부를 중지한 시각입니다. 차례대로 번갈아가면서 [시작 시각, 중지 시각, 시작 시각, 중지 시각, ..., 중지 시각] 형태로 주어집니다. 이때 실제로 공부한 시간을 구하려 합니다.

어플리케이션의 기록을 담은 문자열 배열 log가 매개변수로 주어졌을 때, 실제로 공부한 시간을 HH:MM 형태로 return 하도록 solution 함수를 완성해주세요.

HH:MM형태는 시:분을 뜻합니다. 이때 시혹은 분이 한 자리 수라면 왼쪽에 0을 채워 항상 두 자리가 되게 합니다.
"""

def getTimeDif(start, end):
    startHour, startMinute = list(map(int, start.split(':')))
    endHour, endMinute = list(map(int, end.split(':')))
    
    return (endHour*60 + endMinute) - (startHour*60+startMinute)

def solution(log):
    totalTime = 0
    for i in range(0,len(log), 2):
        studyTime = getTimeDif(log[i], log[i+1])

        if 5 <= studyTime <= 105:
            totalTime += studyTime
        elif 105 < studyTime:
            totalTime += 105

    hour = str(totalTime // 60)
    hour = hour if len(hour) == 2 else '0'+hour
    minute = str(totalTime % 60)
    minute = minute if len(minute) == 2 else '0'+minute
    
    answer = hour + ':' + minute
    return answer

print(solution(["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]))
