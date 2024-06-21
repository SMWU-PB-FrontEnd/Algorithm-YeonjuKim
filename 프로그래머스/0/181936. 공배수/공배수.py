def solution(number, n, m):
    
    restN = number%n
    restM = number%m
    
    answer = 0
    
    if (restN == 0 and restM == 0) : answer = 1
    else : answer = 0
    
    return answer