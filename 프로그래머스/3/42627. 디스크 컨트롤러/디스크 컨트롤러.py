# [작업 요청 시점, 작업 소요 시간]
# 작업 요청부터 종료까지의 평균 시간을 가장 줄이기

# 작업 완료 시간 : 현재 시간 + 소요 시간
# 작업 대기 시간 : 작업 완료 시간 - 작업 요청 시간
# 모든 작업의 평균 대기 시간 최소화

# SJF - Shortest Job First
# SRTF - Shortest Remaining Time First

# 작업 순서 최적화, 소요 시간이 짧은 순서대로 처리

import heapq

def solution(jobs):
    
    # 작업 요청 시간 순서대로 정렬
    jobs.sort()
    
    # 현재 시간
    time = 0
    # 총 대기 시간
    total_wait = 0
    # 작업 총 갯수
    job_count = len(jobs)
    # 현재 수행할 작업 인덱스
    job_index = 0
    # 대기 리스트, 힙(우선순위 큐)
    heap = []
    
    # 현재 수행할 작업 인덱스가, 작업 총 갯수보다 작거나,
    # heap이 존재한다면
    # 즉, 모든 작업이 처리되지 않았거나, 대기 중인 작업이 존재한다면
    while job_index < job_count or heap :
        
        # 현재 수행할 작업 인덱스가, 작업 총 갯수보다 작고,
        # 현재 수행 작업 인덱스의 작업 요청 시간이 현재 시간보다 이르다면,
        # 즉, 수행할 작업이 남아 있고, 해당 작업이 이미 요청된 작업이라면
        while job_index < job_count and jobs[job_index][0] <= time:
            
            # 현재 시간까지 도착한 모든 작업(소요 시간, 요청 시간)을 heapq에 저장
            heapq.heappush(heap, (jobs[job_index][1], jobs[job_index][0]))
            
            # 수행 작업 인덱스 증가
            job_index += 1
            
        # 힙이 비어 있으면
        # 즉 대기 중인 작업이 없다면
        if not heap:
            
            # 다음 작업의 요청 시간으로 현재 시간 이동
            time = jobs[job_index][0]
            continue
            
        # heapq에서 소요 시간이 가장 짧은 작업 pop
        job_dur, job_req = heapq.heappop(heap)
        
        # 현재 시간 업데이트, 총 대기 시간 계산
        time += job_dur
        total_wait += time - job_req
    
    return total_wait // job_count
            


# sort()