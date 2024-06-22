def solution(a, b):
    
    answer = 0
    
    restA=a%2
    restB=b%2
    
    if (restA==1 and restB==1) :
        answer = a**2 + b**2
    elif (restA==1 or restB==1) :
        answer = 2*(a+b)
    else : answer = abs(a-b)
    
    

    return answer