# 해시맵 생성 : completion 리스트의 요소를 카운트 - 선수명, 완주 횟수 저장
# 참여자 리스트 순회 : participant 리스트 순회 - 각 선수의 해시맵 등장 횟수 확인

from collections import Counter

def solution(participant, completion):
    
    completion_count = Counter(completion)
    
    for player in participant :
        # 만약 특정 참여자에 대해 카운트가 0이면, 해당 참여자가 완주 못한 선수임.
        if completion_count[player] == 0: answer = player
        
        # 순회 시마다 -1을 수행해 이름이 같은 선수들 처리
        completion_count[player] -= 1
    
    return answer


# collections
# 파이썬의 범용 내장 컨테이너 dictionary, list, set, tuple에 대한 대안을 제공하는 특수 컨테이너 데이터형 구현 모듈
# namedtuple(), deque, ChainMap, Counter, OrderedDict, defaultdict, UserDict, UserList, UserString


# Counter
# 해시 가능 객체를 위한 dictionary 하위 클래스
# 요소들이 dictionary key로 저장, 그들의 counts가 value로 저장
# 0, 음수를 포함한 모든 정수값을 취급

# 요소(key)는 iterable로부터 계산 or 다른 매핑에서 초기화
# 누락된 요소(key)에 대해 KeyError가 아닌 0을 반환함 (dictionary와의 차이점 - 해당 key가 없을 때 keyError 반환)
# count를 0으로 설정해도 Counter에서 요소(key)가 제거되지 않음. 제거를 위해서는 del 이용.
# elements(), most_common([n]), subtract([Counter]), total()


# iterable
# 반복 가능한. 즉 '객체'
# 순서형 자료형 + 컬렉션 자료형
# string, list, tuple, range(), set, dictionary
# 당연히 반복문 사용 가능

# iterator : iterable한 객체로 생성된 객체
# generator : iterator로 생성된 함수

