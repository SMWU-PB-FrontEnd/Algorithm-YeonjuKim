# 전화번호 집합 생성 (같은 길이의 전화번호 고려)
# 현재 전화번호를 접두어로 갖는 다른 전화번호가 있는지 탐색

def solution(phone_book):
    
    phone_set = set(phone_book)
    
    for phone in phone_book:
        
        # 현재 전화번호의 모든 접두어를 검사(순회)
        for i in range(1, len(phone)):
            if phone[:i] in phone_set:
                return False
    
    return True