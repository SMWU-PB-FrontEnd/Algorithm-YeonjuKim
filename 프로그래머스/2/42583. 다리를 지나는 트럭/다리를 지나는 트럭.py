# bridge_length = 다리 길이, 트럭 한 대가 다리를 건너는 데 걸리는 초 수
# 다리 위 트럭 무게 합 <= weight

# 트럭 대기 큐 : 트럭 대기, 다리 위 운행 상태 관리(추적)
# 다리 위 트럭 큐 : 다리 위 트럭, 해당 트럭 다리 위 운행 시간 관리(추적)
# 경과 시간, 다리 위 트럭 무게 합 관리(추적)

from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    # 트럭 대기 큐
    wait_trucks = deque(truck_weights)
    
    # 다리 위 트럭 큐
    # [0] * bridge_length :
    # bridge_length만큼의 길이를 갖는 리스트 생성, 0으로 초기화
    bridge = deque([0] * bridge_length)
    
    # 다리 위 현재 무게
    current_weight = 0
    
    # 경과 시간
    time = 0
    
    # 대기 트럭이 있거나 다리 위 운행 중인 트럭이 있을 경우
    while wait_trucks or current_weight > 0:
        
        # 트럭이 다리를 다 지나면,
        # 다리 위 트럭 무게 합에서 그만큼 빼기
        current_weight -= bridge.popleft()
        
        # 대기 트럭이 있을 경우
        if wait_trucks :
            
            next_truck = wait_trucks[0]
            
            # 현재 다리 위 트럭 무게와 맨 앞 대기 트럭 무게 합이
            # 다리가 견딜 수 있는 무게보다 작다면
            if current_weight + next_truck <= weight:
                
                # 대기 큐에서 맨 앞 트럭을 popleft
                # 다리 위 큐에 해당 트럭을 append
                # 현재 다리 위 트럭 무게에 해당 트럭 무게만큼 더하기
                truck = wait_trucks.popleft()
                bridge.append(truck)
                current_weight += truck
                
            # 현재 다리 위 트럭 무게와 맨 앞 대기 트럭 무게 합이
            # 다리가 견딜 수 있는 무게보다 크다면
            # 대기 큐는 그대로,
            # 다리 위 큐에는 0을 append
            else :
                bridge.append(0)
                
        # 대기 트럭이 없을 경우
        else : 
            bridge.append(0)
            
        # 시간 증가
        time += 1

    return time