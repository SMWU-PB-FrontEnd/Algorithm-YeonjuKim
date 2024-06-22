def solution(myString, pat):
    answer = 0
    
    switch = myString.translate(str.maketrans("AB","BA"))
                                
    print(switch)
    
    if pat in switch : answer = 1
    else : answer = 0
                                
    return answer