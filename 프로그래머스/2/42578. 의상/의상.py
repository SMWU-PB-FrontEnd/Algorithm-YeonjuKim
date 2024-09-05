# 옷 종류별로 그룹화
# 각 종류별 조합 수 계산
# 조합의 곱 계산

from collections import defaultdict

def solution(clothes):
    
    clothes_dict = defaultdict(list)
    for item, category in clothes:
        clothes_dict[category].append(item)
        
    total_combinations = 1
    for category in clothes_dict :
        # 해당 종류 옷을 입지 않는 것까지 포함(+1)해 조합
        total_combinations *= len(clothes_dict[category]) + 1  
        
        # 아무것도 입지 않는 경우 제외
    return total_combinations -1


# defaultdict
# dictionary class의 하위 클래스.
# 유사 dictionary 객체 리턴.
# 인자로 주어진 객체 기본값(default_factory)을 dictionary value 초깃값으로 지정 가능
# ex) d = defaultdict(list)이면, 기본값인 빈 list 생성. 
# 모든 key에 대해, 값이 없는 경우, 자동으로 생성자의 인자로 넘어온 함수를 호출, 그 결과값을 기본값으로 설정.
# 값이 존재하지 않는 key값에 기본값 설정을 해주기 때문에 에러가 발생하지 않음.