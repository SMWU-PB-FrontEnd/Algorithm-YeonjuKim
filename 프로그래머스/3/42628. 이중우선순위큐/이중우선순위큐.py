# 최댓값, 최솟값을 전부 관리하기 위해
# 최대 힙, 최소 힙 전부 사용
# 삽입/삭제 연산

import heapq

def solution(operations):
    
    # 최대 힙, 최소 힙 
    max_heap = []
    min_heap = []
    
    for operation in operations:
        
        # 숫자 삽입 시
        if operation.startswith('I'):
            
            num = int(operation.split()[1])
            
            # 최소 힙에 삽입
            heapq.heappush(min_heap, num)
            # 최대 힙에 삽입
            # 파이썬의 heapq는 최소 힙을 지원하므로, 
            # 최댓값을 빠르게 꺼내는 구조로 바꾸기 위해 모든 값을 음수로 변환해 힙에 저장.
            # 그러면 가장 큰 값이 가장 작은 값으로 바뀌므로 해당 값을 최소 힙 맨 위에 배치시킬 수 있음.
            heapq.heappush(max_heap, -num)
            
        # 최댓값 삭제 시
        elif operation == 'D 1':
            if max_heap:
                max_value = heapq.heappop(max_heap)
                min_heap.remove(-max_value)
                
        # 최솟값 삭제 시
        elif operation == 'D -1':
            if min_heap:
                min_value = heapq.heappop(min_heap)
                max_heap.remove(-min_value)
                
    if not min_heap or not max_heap:
        return [0,0]
    else:
        return [-max_heap[0], min_heap[0]]


# startswith(), endswith()
# 대상 문자열의 시작/끝이 지정된 문자와 같은지 boolean 리턴
# s.startswith('a')
