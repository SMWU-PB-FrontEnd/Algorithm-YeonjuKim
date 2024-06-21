def solution(a, b):
    
    ab = str(a)+str(b)
    ba = str(b)+str(a)
 
    answer = ''
    
    if (ab >= ba) : answer = int(ab)
    else : answer = int(ba)
    
    return answer