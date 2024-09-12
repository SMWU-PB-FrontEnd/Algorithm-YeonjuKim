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
    
    for i in range(0, len(progresses)):
        prog = progresses[i]
        speed = speeds[i]
        
        cal = math.ceil((100 - prog)/speed)
        left_days.append(cal)
    
    result = []
    current_deploy_day = left_days[0]
    count = 0
    
    for day in left_days:
        if day <= current_deploy_day:
            count += 1
        else :
            result.append(count)
            current_deploy_day = day
            count = 1
            
    result.append(count)
        
    return result