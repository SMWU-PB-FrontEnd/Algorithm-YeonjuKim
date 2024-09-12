# 선입선출
# 프로세스 중요도 배열 priorities (숫자가 클수록 중요도 높음)
# 프로세스 위치 인덱스 location 

from collections import deque

def solution(priorities, location):
    
    # 빈 큐 생성
    queue = deque()
    
    # priorities 인덱스 기준 반복
    for i in range(0, len(priorities)):
        
        # 해당 인덱스의 값 priorities[i]와 인덱스를 queue에 append
        priority = priorities[i]
        queue.append((priority, i))
    
    
    # location의 실행 순서 초깃값 설정
    answer = 0
    
    # queue가 존재할 때
    while queue:
        
        # priorities 순서에 맞게, 맨 처음 요소부터 pop
        current = queue.popleft()
        
        # 해당 요소보다 큰 우선순위를 가진 다른 요소가 queue에 존재하면
        # 다시 queue에 append
        if any(current[0] < other[0] for other in queue):
            queue.append(current)
        
        # 해당 요소보다 큰 우선순위를 가진 다른 요소가 queue에 없다면
        # 실행 순서 + 1
        else:
            answer += 1
            
            # 만약 해당 요소의 인덱스가 location과 같다면 리턴
            if current[1] == location:
                return answer
    
    return answer




# deque
# iterable 데이터를 받아 양방향 deque 객체 반환
# O(1)
# append(), appendleft()
# pop(), popleft()
# extend(), extendleft()
# clear(), copy(), count(), remove(value), reverse()...

# any 함수
# iterable 데이터를 받아 하나라도 true이면 true
# if 문과 함께 사용 가능
