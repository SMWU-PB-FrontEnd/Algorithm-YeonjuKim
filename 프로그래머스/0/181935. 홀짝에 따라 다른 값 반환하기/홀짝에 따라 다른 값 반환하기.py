def solution(n):
    
    restN = n%2
    
    print(restN)
    
    total = 0
        
    if (restN == 1) :
        for i in range(0, n+1):
            if (i%2 == 1) :
                total += i
    else : 
        for i in range(0, n+1):
            if (i%2 == 0):
                total += i**2
                
    answer = total
    return answer