def solution(a, b):
    
    ab = int(str(a)+str(b))
    ab2 = 2*a*b
    
    answer = 0
    
    if (ab >= ab2 ) : answer = ab
    else : answer = ab2
    
    return answer