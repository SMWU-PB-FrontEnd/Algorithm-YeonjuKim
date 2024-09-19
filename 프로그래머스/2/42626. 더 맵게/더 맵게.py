# 스코빌 지수가 가장 낮은 두 개의 음식
# 가장 작은 스코빌 지수 + 두번째로 작은 스코빌 지수 * 2
# 가장 작은 스코빌 지수가 K 이상이 될 때까지 반복

import heapq

def solution(scoville, K):
    
    # 존재하는 리스트 scoville을 힙으로 변환해 최소 힙 생성
    heapq.heapify(scoville)
    
    # 섞은 횟수
    count = 0
    
    # 스코빌 지수가 K 미만일 때 반복
    while scoville[0] < K :
        
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
        if len(scoville) < 2:
            return -1
        
        # 가장 작은 스코빌 지수, 두번째로 작은 스코빌 지수 pop
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        # 섞은 스코빌 지수
        mixed = first + second*2
        
        # 섞은 스코빌 지수를 추가 
        heapq.heappush(scoville, mixed)
        
        # 섞은 횟수 증가
        count += 1
    
    return count


# heapq
# 내부 요소들을 최소 힙 형태로 정렬

# heapq.heapify(x): 존재하는 리스트를 즉각적으로 heap으로 변환, O(N)
# heapq.heappush(heap, item): item을 heap에 추가
# heapq.heappop(heap): heap에서 가장 작은 원소를 pop, return. 비어 있는 경우 indexError