# 진도 100% 시 서비스 반영
# 각 기능 개발 속도 다르나
# 뒷 기능은 앞 기능 배포 시 함께 배포
# 배포 순서대로 작업 진도가 적힌 정수 배열 progresses
# 각 작업 개발 속도가 적힌 정수 배열 speeds
# 각 배포마다 몇 개의 기능이 배포되는지

# 앞으로 남은 작업량: 100 - progresses[i]
# 앞남작 / speeds -> 나머지 존재하면 + 1 (ceil or divmod 사용)
# 특정 작업이 완료되었을 때, 
# 그 앞 작업 중에 배포되지 않은 것(100%가 아닌 것)이 있나 확인

# 그러니까 남은 일수를 배열로 만들면, 
# 뒷 인덱스에 더 작은 값이 있는 묶음만큼 한꺼번에 배포됨.
# 그 묶음을 배열로 리턴

import math

def solution(progresses, speeds):

    left_days = []
    
    # progresses의 원소 갯수만큼 반복
    for i in range(0, len(progresses)):
        
        # progresses, speeds의 i번째 원소
        prog = progresses[i]
        speed = speeds[i]
        
        # 남은 일자 계산, 배열에 append
        cal = math.ceil((100 - prog)/speed)
        left_days.append(cal)
    
    # 첫 배포일 초깃값은 left_days의 [0]번째 원소 
    result = []
    current_deploy_day = left_days[0]
    count = 0
    
    # left_days 원소를 이용한 반복
    for day in left_days:
        
        # 해당 원소(남은 일 수)가 현재 배포 값(배포까지 남은 일 수)보다 작다면,
        # 해당 배포의 기능 갯수 count + 1
        if day <= current_deploy_day:
            count += 1
            
        # 해당 원소(남은 일 수)가 현재 배포 값(배포까지 남은 일 수)보다 크다면,
        # 현재 남은 일 수가 새로운 배포까지의 남은 일 수가 되고
        # 지금까지의 기능 count는 result에 append,
        # 새로운 배포일에 맞게 기능 count도 1부터 시작
        else :
            result.append(count)
            current_deploy_day = day
            count = 1
            
    # 모든 과정이 끝나면, 최종 count를 result에 append
    result.append(count)
        
    return result