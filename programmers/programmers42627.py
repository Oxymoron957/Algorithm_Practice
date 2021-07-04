'''
디스크 컨트롤러
https://programmers.co.kr/learn/courses/30/lessons/42627
'''

def solution(jobs):
    cur_time = 0
    avg_process_time = 0
    num_of_task = len(jobs)

    while jobs:
        waiting_job = []
        for job in jobs:
            if cur_time >= job[0]:
                waiting_job.append(job)
        if not waiting_job:
            cur_time += 1
            continue    
        
        cur_job = min(waiting_job, key = lambda x : x[1])

        cur_time += cur_job[1] # 요청이 종료된 시간
        start_time = cur_job[0] # 요청이 시작된 시간
        avg_process_time += cur_time- start_time

        jobs.remove(cur_job)
    
    return int(avg_process_time/num_of_task)
        


print(solution([[0, 3], [1, 9], [2, 6]]))