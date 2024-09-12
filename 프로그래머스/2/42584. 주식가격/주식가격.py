# prices의 뒷 인덱스 값 중에 현재 인덱스 값보다 떨어진 경우를 찾기

def solution(prices):
    
    # 주어진 배열의 길이
    n = len(prices)
    
    # 각 가격의 떨어지지 않은 기간을 저장할 배열 result
    result = [0] * n
    
    # 인덱스를 저장할 스택
    stack = []
    
    # 가격 배열 인덱스 기준 순회
    for i in range(n):
        
        # 스택이 존재하고, 현재 가격이 스택의 마지막 가격보다 낮을 경우
        # 계속 반복
        while stack and prices[i] < prices[stack[-1]]:
            
            # 스택에서 해당 인덱스를 pop
            # 해당 인덱스는 현재 가격보다 높은 가격을 가짐
            index = stack.pop()
            
            # 가격이 떨어지지 않은 기간 계산
            result[index] = i - index
            
        # 현재 인덱스를 스택에 추가
        # 이후의 가격과 비교할 것
        stack.append(i)
        
    # 스택에 인덱스가 남아 있을 경우
    # 끝까지 가격이 떨어지지 않은 경우
    while stack :
        
        index = stack.pop()
        
        # 끝까지 떨어지지 않은 기간 계산
        result[index] = n - index - 1
    
    return result