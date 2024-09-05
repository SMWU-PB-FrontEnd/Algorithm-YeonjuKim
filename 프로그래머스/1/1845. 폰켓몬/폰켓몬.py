# 총 n마리, 절반인 n/2 마리

# 파이썬의 set 함수로 포켓몬 종류의 고유한 수 계산
# len(nums)//2(전체의 절반)로 선택 가능한 마릿수 계산
# min(종류 수, 선택 가능 마릿수(절반))으로 선택 가능한 최대 종류 수 계산


def solution(nums):
    
    mon_types = len(set(nums))
    
    can_pick = len(nums) // 2
    
    answer = min(mon_types, can_pick)
    
    return answer



# set 함수 : 중복 불허, 순서 X
# 리스트, 튜플은 순서 O -> 인덱싱 지원 O
# set, 딕셔너리 순서 X -> 인덱싱 지원 X

# set 교집합 : s1 & s2, s1.intersecion(s2)
# set 합집합 : s1 | s2, s1.union(s2)
# set 차집합 : s1 - s2, s1.difference(s2)

# add : 값 1개 추가
# update : 값 여러 개 추가
# remove : 특정 값 제거


# 해시 in 파이썬 : 주로 set, dictionary로 중복 데이터 제거, 고유 데이터를 빠르게 탐색/조회