# stack -> 기존의 가장 마지막 괄호 + 추가될 괄호가 짝이면 pop

def solution(s):

    stack = []
    
    for parentheses in s:
        # 문자가 (이면 stack에 추가
        if parentheses == '(':
            stack.append(parentheses)
        else:
            # 문자가 )이고, stack에 (가 존재하면, 
            # stack의 가장 마지막 (를 pop
            if stack:
                stack.pop()
            # stack에 (가 남아있지 않다면 false
            else:
                return False

    # 모든 pop이 완료된 stack의 길이가 0 이라면 true 
    return len(stack) == 0